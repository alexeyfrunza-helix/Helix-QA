import zipfile
import os
import sys

collectedReleaseP = sys.argv[1]

# Путь к .rar файлу и папке для извлечения
zip_path = rf'{collectedReleaseP}\setup.zip'
extract_dir = rf'{collectedReleaseP}'

# Убедитесь, что директория для извлечения существует
os.makedirs(extract_dir, exist_ok=True)

# Открытие и разархивирование
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("Архив .rar успешно разархивирован.")

