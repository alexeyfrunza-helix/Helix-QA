import subprocess
import sys

collectedReleaseP = sys.argv[1]
# Путь к установочному файлу 1С
path_to_installer = rf'{collectedReleaseP}\setup.exe'

# Запуск установочного файла 1С через Python
subprocess.run([path_to_installer, '/S'], shell=True)

