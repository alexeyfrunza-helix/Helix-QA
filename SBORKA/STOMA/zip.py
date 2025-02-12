import zipfile
import os
import sys

fbrb = sys.argv[1]
target_path = sys.argv[2] 
def zip_selected_files(file_paths, archive_name):
    """
    Архивирует выбранные файлы в указанный архив.

    :param file_paths: Список полных путей к файлам, которые нужно заархивировать.
    :param archive_name: Имя архива, куда будут добавлены файлы.
    """
    with zipfile.ZipFile(archive_name, 'w') as archive:
        for file_path in file_paths:
            if os.path.exists(file_path):
                archive.write(file_path, os.path.basename(file_path))
                print(f"Файл {file_path} добавлен в архив {archive_name}.")
            else:
                print(f"Файл {file_path} не найден и не был добавлен.")

# Пример использования
directory_path = rf'{fbrb}'
selected_files = [
    os.path.join(directory_path, '4FB1.datafile'),
    os.path.join(directory_path, '4FB1.paramfile')
]
archive_name = rf'{target_path}\Комплект первичных материалов\KeyDB\4FB1.zip'

zip_selected_files(selected_files, archive_name)
