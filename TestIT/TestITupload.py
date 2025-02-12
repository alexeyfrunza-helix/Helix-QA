import testit_api_client
import os
import subprocess
import sys

#allureResultsDir = sys.argv[1]
#jOB_NAME = sys.argv[2]
# Установите ваш токен, URL, и параметры
TMS_TOKEN = "S09XeFE5akJyeVltYUx2T3pp"
INSTANCE_URL = "https://team-x62t.testit.software/"
PROJECT_ID = "536ab7c2-97b2-4646-b9d5-ad6348547c15"
CONFIGURATION_ID = "30f423ac-fb0f-4f06-8c12-281a99d3fc19"
TEST_RUN_ID = "d9227160-3391-4408-84c7-c21134fcbfa0"
#TESTRUN_NAME = "TestNG test run"
#RESULTS_PATH = rf"{allureResultsDir}\junit.xml"
RESULTS_PATH = r"C:\jENKINS\workspace\FITNESS_debug\results\junit.xml"
# Экспорт токена в переменные окружения
os.environ["TMS_TOKEN"] = TMS_TOKEN

# Формирование команды для импорта результатов
command = [
    "testit",
    "results",
    "import",
    "--url", INSTANCE_URL,
    "--project-id", PROJECT_ID,
    "--configuration-id", CONFIGURATION_ID,
    "--testrun-id", TEST_RUN_ID,
#    "--testrun-name", jOB_NAME,
    "--results", RESULTS_PATH
]

try:
    # Выполнение команды
    subprocess.run(command, check=True)
    print("Результаты успешно импортированы!")
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения команды: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
