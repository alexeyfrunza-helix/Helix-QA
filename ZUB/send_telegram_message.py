import requests

telegram_bot_token = '7117726988:AAFJFXz3rF7XyNXK23vtcy6MQG1E9x3DmRc'
chat_id = '-1002167629740'
message = "Зубная формула загружена успешно"

# Отправка сообщения с текстом "Зубная формула загружена успешно" в групповой чат тестеров.
def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Отправка сообщения
response = send_telegram_message(telegram_bot_token, chat_id, message)
print(response)
