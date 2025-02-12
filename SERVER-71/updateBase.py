# Обновляет базу с релизного хранилища
import sys
import os
import subprocess

# Получаем значения из аргументов командной строки
platformPath = sys.argv[1]
vaBase = sys.argv[2]
vaUser = sys.argv[3]
repositoryReleaseFitness = sys.argv[4]
repositoryUser = sys.argv[5]

def update_configuration():
    # Устанавливаем кодировку в UTF-8
    os.system('chcp 65001')

    # Проверка наличия исполняемого файла
    if not os.path.isfile(platformPath):
        print(f"Executable not found: {platformPath}. Please check the path and try again.")
        return

    # Формируем команду для выполнения
    command = [
        rf"{platformPath}",
        "DESIGNER",
        "/ConfigurationRepositoryUpdateCfg",
        "-revised",
        "-force",
        "/DepotUpdateCfg",
        "/UpdateDBCfg",
        f"/S {vaBase}",
        f"/N {vaUser}",
        f"/ConfigurationRepositoryF {repositoryReleaseFitness}",
        f"/ConfigurationRepositoryN {repositoryUser}"
    ]

    # Печатаем команду для отладки
    print("Executing command:", " ".join(command))

    try:
        # Выполняем команду
        result = subprocess.run(command, text=True, check=True)
        
        # Проверяем успешность выполнения
        if result.returncode == 0:
            print("Configuration update successful")
    except subprocess.CalledProcessError as e:
        print(f"Configuration update failed with code {e.returncode}")
        print("Error output:", e.output)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Вызываем функцию
update_configuration()
