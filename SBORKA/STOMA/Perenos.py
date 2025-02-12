import os
import shutil
import zipfile
import sys
import shutil

newversion_1 = sys.argv[1]
target_path = sys.argv[2]
collectedReleaseP = sys.argv[3]
oldCF = sys.argv[4]
collectedReleaseOb = sys.argv[5]
fbrb = sys.argv[6]

# Формирование дополнительных переменных для версии
def create_version_variables(version):
    parts = version.split('.')
    version_3 = '_'.join(parts)
    return version_3

newversion_3 = create_version_variables(newversion_1)

# Перенос файлов установки поставки обновления  ('1cv8.efd', 'setup', 'setup.exe') из папки сборки в  Комплект поставки обновления\Updsetup # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def move_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Переносим каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Файл {filename} перенесен в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

source_folder = rf'{collectedReleaseOb}\update'   # Исходная папка
destination_folder = rf'{target_path}\Комплект поставки обновления\Updsetup' # Папка назначения
filenames = ['1cv8.efd', 'setup', 'setup.exe']  # Имена файлов
move_specific_files(source_folder, destination_folder, filenames)


# Перенос файлов установки полной поставки  ('1cv8.efd', 'setup', 'setup.exe') из папки сборки в \Дистрибутив\Configs\Stomatology\Setup # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def move_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Переносим каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Файл {filename} перенесен в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

source_folder = rf'{collectedReleaseP}'
destination_folder = rf'{target_path}\Дистрибутив\Configs\Stomatology\Setup'
filenames = ['1cv8.efd', 'setup', 'setup.exe']  # Имена файлов
move_specific_files(source_folder, destination_folder, filenames)


# Перенос файла 1Cv8.dt из шаблона установленной основной поставки в \Комплект первичных материалов\DemoDB  # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def move_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Переносим каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Файл {filename} перенесен в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

source_folder = rf'C:\Users\y.fateeva\AppData\Roaming\1C\1c8\tmplts\helix\stomatology\{newversion_3}'
destination_folder = rf'{target_path}\Комплект первичных материалов\DemoDB'
filenames = ['1Cv8.dt']  # Имена файлов
move_specific_files(source_folder, destination_folder, filenames)


# Перенос файла "Файл описания комплекта поставки.edf" в Комплект первичных материалов  # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def copy_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Копируем каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.copy2(source_file, destination_file)  # Копируем файл
            print(f"Файл {filename} скопирован в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

# Пример использования
source_folder = rf'{fbrb}'
destination_folder = rf'{target_path}\Комплект первичных материалов'
filenames = ['Файл описания комплекта поставки.edf']  # Имена файлов
copy_specific_files(source_folder, destination_folder, filenames)


# Перенос файла Helix.epf  в Комплект первичных материалов\Sources # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def move_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Переносим каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Файл {filename} перенесен в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

source_folder = rf'{fbrb}'
destination_folder = rf'{target_path}\Комплект первичных материалов\Sources'
filenames = ['Helix.epf']  # Имена файлов
move_specific_files(source_folder, destination_folder, filenames)




# Перенос файла 1Cv8.cf из шаблона установленной основной поставки в папку с старыми версияеми  # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def move_specific_files(source_folder, destination_folder, filenames):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не найдена.")
        return
    
    # Проверяем, существует ли целевая папка, если нет - создаем
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Переносим каждый файл из списка
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        
        # Проверяем, существует ли файл
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Файл {filename} перенесен в {destination_folder}")
        else:
            print(f"Файл {filename} не найден в {source_folder}")

source_folder = rf'C:\Users\y.fateeva\AppData\Roaming\1C\1c8\tmplts\helix\stomatology\{newversion_3}'
destination_folder = rf'{oldCF}'
filenames = ['1Cv8.cf']  # Имена файлов
move_specific_files(source_folder, destination_folder, filenames)


# Переименовывает 1Cv8.cf в актуальную версию релиза  # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def find_and_rename_file(folder_path, old_name_pattern, new_name):
    # Проверяем, существует ли папка
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не найдена.")
        return
    
    # Перебираем файлы в папке
    for filename in os.listdir(folder_path):
        # Проверяем, содержит ли имя файла нужный шаблон (или является точным именем)
        if old_name_pattern in filename:
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)

            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            print(f"Файл {filename} переименован в {new_name}")
            return

    print(f"Файл, содержащий {old_name_pattern}, не найден.")

folder_path = rf'{oldCF}'
old_name_pattern = '1Cv8.cf'  # Например, ищем файл, содержащий 'setup'
new_name = rf'{newversion_1}.cf'  # Новое имя файла
find_and_rename_file(folder_path, old_name_pattern, new_name)


# Архивирует дистрибутив # 
# # # # # # # # # # # #  # 

def zip_all_files_and_folders(directory_path, archive_name):
    """
    Архивирует все файлы и папки, включая содержимое подкаталогов, из указанной директории.

    :param directory_path: Путь к директории, файлы и папки которой нужно заархивировать.
    :param archive_name: Имя архива, куда будут добавлены файлы и папки.
    """
    if not os.path.exists(directory_path):
        print(f"Папка {directory_path} не найдена.")
        return

    with zipfile.ZipFile(archive_name, 'w') as archive:
        # os.walk проходит по директории и всем её подкаталогам
        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Добавляем файл в архив с относительным путём
                archive.write(file_path, os.path.relpath(file_path, directory_path))
                print(f"Файл {file_path} добавлен в архив {archive_name}.")
            
            for subfolder in subfolders:
                folder_path = os.path.join(foldername, subfolder)
                # Добавляем пустую папку, если она есть
                if not os.listdir(folder_path):  # Проверяем, пустая ли папка
                    folder_zip_path = os.path.relpath(folder_path, directory_path) + '/'
                    archive.write(folder_path, folder_zip_path)
                    print(f"Папка {folder_path} добавлена в архив {archive_name}.")

directory_path = rf'{target_path}\Дистрибутив'
archive_name = rf'D:\STOMA_release_build\Стоматологическая клиника {newversion_1}.zip'
zip_all_files_and_folders(directory_path, archive_name)