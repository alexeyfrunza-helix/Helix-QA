import requests
import logging
from logging.handlers import RotatingFileHandler
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import TOKEN, JENKINS_URL, JENKINS_USER, JENKINS_API_TOKEN

# Настройка логирования: вывод в консоль и запись в файл с ротацией
log_handler = RotatingFileHandler(
    "C:\\logs\\bot_logs.txt",
    maxBytes=5*1024*1024,  # 5 MB
    backupCount=1,         # Хранить 1 старых файлов
    encoding='utf-8'
)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.basicConfig(level=logging.INFO, handlers=[
    log_handler,
    logging.StreamHandler()
])

def get_jenkins_views():
    """Получение списка всех доступных Jenkins Views."""
    url = f'{JENKINS_URL}/api/json?tree=views[name,url]'
    auth = (JENKINS_USER, JENKINS_API_TOKEN)
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Response from Jenkins API: {data}")
        
        # Фильтрация, чтобы исключить view с именем 'all'
        views = [view for view in data.get('views', []) if view['name'] != 'all']
        return views
        
    except requests.RequestException as e:
        logging.error(f"Error fetching Jenkins views: {e}")
        return []

def get_jenkins_jobs(view_name: str):
    """Получение списка всех доступных Jenkins Jobs в определенном представлении."""
    url = f'{JENKINS_URL}/view/{view_name}/api/json?tree=jobs[name]'
    auth = (JENKINS_USER, JENKINS_API_TOKEN)
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json().get('jobs', [])
    except requests.RequestException as e:
        logging.error(f"Error fetching Jenkins jobs: {e}")
        return []

async def start(update: Update, context: CallbackContext):
    """Отправка списка Jenkins Views как кнопок в Telegram."""
    if update.message.chat_id < 0:
        return  # Игнорируем сообщения из групповых чатов

    user_id = update.message.from_user.id
    username = update.message.from_user.username

    try:
        views = get_jenkins_views()
        if not views:
            await update.message.reply_text('Failed to retrieve Jenkins views.')
            return

        # Формируем клавиатуру с именами Views
        keyboard = [[view['name']] for view in views]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text('Выберите раздел:', reply_markup=reply_markup)
        context.user_data['current_menu'] = 'views'  # Сохраняем текущее меню

        logging.info(f"User {username} (ID: {user_id}) started the bot and received the list of views.")

    except Exception as e:
        logging.error(f"Exception in start handler: {e}")
        await update.message.reply_text('Произошла ошибка. Пожалуйста, попробуйте позже.')

async def handle_message(update: Update, context: CallbackContext):
    """Обработка сообщений и запуск Job."""
    if update.message.chat_id < 0:
        return  # Игнорируем сообщения из групповых чатов

    user_id = update.message.from_user.id
    username = update.message.from_user.username

    user_choice = update.message.text
    current_menu = context.user_data.get('current_menu')

    # Если сообщение не в 'views' и 'jobs', возвращаем в главное меню
    if current_menu not in ['views', 'jobs']:
        await start(update, context)
        return
    
    try:
        if current_menu == 'views':
            # Обработка выбора view
            jobs = get_jenkins_jobs(user_choice)
            if not jobs:
                await update.message.reply_text(f'No jobs found in view {user_choice}.')
                logging.info(f"User {username} (ID: {user_id}) selected view {user_choice}, but no jobs were found.")
                return

            # Формируем клавиатуру с именами Jobs и кнопкой "Назад"
            keyboard = [[job['name']] for job in jobs]
            keyboard.append(['Back'])  # Добавляем кнопку "Назад" только в меню Jobs

            reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            await update.message.reply_text(f'Раздел {user_choice}:', reply_markup=reply_markup)
            context.user_data['current_menu'] = 'jobs'
            context.user_data['selected_view'] = user_choice

            logging.info(f"User {username} (ID: {user_id}) selected view {user_choice} and received the list of jobs.")

        elif current_menu == 'jobs':
            if user_choice == 'Back':
                # Возвращаемся в главное меню
                await start(update, context)
                logging.info(f"User {username} (ID: {user_id}) chose to go back to the main menu.")
                return

            job_name = user_choice
            chat_id = update.message.chat_id

            # Определяем URL для запуска Job
            url_with_chat_id = f'{JENKINS_URL}/job/{job_name}/buildWithParameters?chat_id={chat_id}'
            url_without_chat_id = f'{JENKINS_URL}/job/{job_name}/build'

            auth = (JENKINS_USER, JENKINS_API_TOKEN)
            try:
                # Попытка запуска Job с параметром chat_id
                response = requests.post(url_with_chat_id, auth=auth)
                response.raise_for_status()
                await update.message.reply_text(f'{job_name} запущена успешно!')
                logging.info(f"User {username} (ID: {user_id}) started job {job_name} with chat_id {chat_id}.")
            except requests.HTTPError as e:
                if response.status_code == 404:
                    # Ошибка 404 - возвращаемся в главное меню
                    await start(update, context)
                    logging.error(f"Error 404 while starting job {job_name}. Returning to main menu.")
                elif response.status_code == 500:
                    # Ошибка 500 - пробуем запустить Job без параметра chat_id
                    try:
                        response = requests.post(url_without_chat_id, auth=auth)
                        response.raise_for_status()
                        await update.message.reply_text(f'{job_name} запущена успешно без параметра chat_id!')
                        logging.info(f"User {username} (ID: {user_id}) started job {job_name} without chat_id.")
                    except requests.RequestException as e:
                        logging.error(f"Error launching job {job_name} without chat_id: {e}")
                        await update.message.reply_text(f'Ошибка при запуске {job_name}. Error: {e}')
                else:
                    logging.error(f"Error launching job {job_name}: {e}")
                    await update.message.reply_text(f'Ошибка при запуске {job_name}. Error: {e}')
                return
            
    except Exception as e:
        logging.error(f"Exception in handle_message handler: {e}")
        await update.message.reply_text('Произошла ошибка. Пожалуйста, попробуйте позже.')

def main():
    """Основная функция для запуска бота."""
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд и сообщений
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    logging.info('Bot is starting...')
    application.run_polling()

if __name__ == '__main__':
    main()
