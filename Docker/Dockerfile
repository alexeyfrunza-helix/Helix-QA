FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Установка Chocolatey
RUN powershell -NoProfile -ExecutionPolicy Bypass -Command \
    Set-ExecutionPolicy Bypass -Scope Process -Force; \
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установка Java
RUN choco install openjdk11 -y

# Установка 1С (пример для серверной части, укажи свой путь к дистрибутиву)
#COPY setup_1c.exe C:\setup_1c.exe
#RUN C:\setup_1c.exe /S /D="C:\Program Files\1cv8"

# Установка Vanessa Automation
RUN choco install vanessa-automation -y

# Установка Allure
RUN choco install allure -y

# Установка Git (если нужно)
RUN choco install git -y

# Установка дополнительных зависимостей (по необходимости)
# RUN choco install some-package -y

# Установка пути для выполнения команд в контейнере
ENV PATH="C:\\Program Files\\1cv8;C:\\Program Files\\Vanessa-Automation;C:\\Program Files\\OpenJDK11\\bin;%PATH%"

CMD ["powershell"]