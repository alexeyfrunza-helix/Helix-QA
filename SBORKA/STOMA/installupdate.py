import subprocess
import sys

collectedReleaseOb = sys.argv[1]

# Путь к установочному файлу 1С
path_to_installer = rf'{collectedReleaseOb}\update\setup.exe'

# Запуск установочного файла 1С через Python
subprocess.run([path_to_installer, '/S'], shell=True)

