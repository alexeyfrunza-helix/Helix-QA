import os
import shutil
import fnmatch
import logging
import sys

sys.stdout.reconfigure(encoding='utf-8')
# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Обработчик для записи логов в файл
file_handler = logging.FileHandler('deletion_log.log')
file_handler.setLevel(logging.INFO)

# Обработчик для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Формат для логирования
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики в логгер
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Пути к папкам
target_path = None #r"D:\SBORKA\Stomatology"
target_path = sys.argv[1]

# Папки, которые нужно удалить
folders_to_delete = [
    os.path.join(target_path, r"Комплект поставки обновления\Updsetup"),
    os.path.join(target_path, r"Комплект первичных материалов\Update")
]

# Файлы, которые нужно удалить
files_to_delete = ["1Cv8.dt", "1cv8.efd", "setup.exe", "setup"]

# Удаление папок с их содержимым
for folder in folders_to_delete:
    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
            logger.info(f"Папка удалена: {folder}")
        except Exception as e:
            logger.error(f"Ошибка при удалении папки {folder}: {str(e)}")
    else:
        logger.warning(f"Папка не найдена: {folder}")

# Удаление файлов в целевом каталоге
for root, dirs, files in os.walk(target_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Удаление файлов по списку и по маске "Идентификатор_*"
        if file in files_to_delete or fnmatch.fnmatch(file, 'Идентификатор_*'):
            try:
                os.remove(file_path)
                logger.info(f"Файл удален: {file_path}")
            except Exception as e:
                logger.error(f"Ошибка при удалении файла {file_path}: {str(e)}")
        
        # Удаление файлов с расширением .xls
        if file.endswith('.xls'):
            try:
                os.remove(file_path)
                logger.info(f".xls файл удален: {file_path}")
            except Exception as e:
                logger.error(f"Ошибка при удалении .xls файла {file_path}: {str(e)}")
