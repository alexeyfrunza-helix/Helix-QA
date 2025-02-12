@echo off
chcp 65001 >nul
setlocal

:: Определение цветов
set "COLOR_MENU=0A"  :: Зеленый текст на черном фоне
set "COLOR_ERROR=0C" :: Красный текст на черном фоне
set "COLOR_RESET=0F" :: Белый текст на черном фоне

:start

:: Определение путей для каждого продукта
:: FITNESS
set "path1_1=C:\\github\\VAFitness\\FITNESS"
set "path2_1=C:\\github\\VAFitness\\FITNESS\\Оплаты "
set "path3_1=C:\\github\\VAFitness\\FITNESS\\Занятия"
set "path4_1=C:\\github\\VAFitness\\FITNESS\\Триггерные события"
set "path5_1=C:\\github\\VAFitness\\FITNESS\\test"
set "path6_1=C:\\github\\VAFitness\\FITNESS\\test"
set "path7_1=C:\\github\\VAFitness\\FITNESS\\test"
set "path9_1=C:\\github\\VAFitness\\smoke\\fitness"

set "dbName_1=VAFitness"

:: SALON
set "path1_2=C:\\github\\VAFitness\\SALON"
set "path2_2=C:\\github\\VAFitness\\SALON\\Оплаты"
set "path3_2=C:\\github\\VAFitness\\SALON\\Клиент"
set "path4_2=C:\\github\\VAFitness\\SALON\\Визит"
set "path5_2=C:\\github\\VAFitness\\SALON\\Справка в налоговую"
set "path6_2=C:\\github\\VAFitness\\SALON\\Уведомления"
set "path7_2=C:\\github\\VAFitness\\SALON\\test"
set "path9_2=C:\\github\\VAFitness\\smoke\\salon"

set "dbName_2=VASPA"

:: STOMA
set "path1_3=C:\\github\\VAFitness\\STOMA"
set "path2_3=C:\\github\\VAFitness\\STOMA\\Оплаты"
set "path3_3=C:\\github\\VAFitness\\STOMA\\Маркетинговые акции"
set "path4_3=C:\\github\\VAFitness\\STOMA\\test"
set "path5_3=C:\\github\\VAFitness\\STOMA\\test"
set "path6_3=C:\\github\\VAFitness\\STOMA\\test"
set "path7_3=C:\\github\\VAFitness\\STOMA\\test"
set "path9_3=C:\\github\VAFitness\\smoke\\stoma"

set "dbName_3=VAStoma"

:selectProduct
cls
color %COLOR_MENU%
echo ============================================
echo         Выберите продукт для тестирования:
echo ============================================
echo 1. FITNESS
echo 2. SALON
echo 3. STOMA
echo ============================================
echo 0. Назад/Выход
echo ============================================

:: Ожидание нажатия клавиши
choice /c 0123 /n >nul

:: Проверка выбора
if errorlevel 1 if not errorlevel 2 goto :exit
if errorlevel 2 if not errorlevel 3 (
    set "path1=%path1_1%"
    set "path2=%path2_1%"
    set "path3=%path3_1%"
    set "path4=%path4_1%"
    set "path5=%path5_1%"
    set "path6=%path6_1%"
    set "path7=%path7_1%"
    set "path9=%path9_1%"
    set "productType=FITNESS"
    set "dbName=%dbName_1%"
) else if errorlevel 3 if not errorlevel 4 (
    set "path1=%path1_2%"
    set "path2=%path2_2%"
    set "path3=%path3_2%"
    set "path4=%path4_2%"
    set "path5=%path5_2%"
    set "path6=%path6_2%"
    set "path7=%path7_2%"
    set "path9=%path9_2%"
    set "productType=SALON"
    set "dbName=%dbName_2%"
) else if errorlevel 4 (
    set "path1=%path1_3%"
    set "path2=%path2_3%"
    set "path3=%path3_3%"
    set "path4=%path4_3%"
    set "path5=%path5_3%"
    set "path6=%path6_3%"
    set "path7=%path7_3%"
    set "path9=%path9_3%"
    set "productType=STOMA"
    set "dbName=%dbName_3%"
)

:menu
:: Удаление файла VAParams.json перед выбором
if exist VAParams.json (
    del VAParams.json
)
cls
cls
color %COLOR_MENU%
echo ============================================
echo          Выберите раздел тестирования:
echo ============================================
echo 1. %path1%
echo 2. %path2%
echo 3. %path3%
echo 4. %path4%
echo 5. %path5%
echo 6. %path6%
echo 7. %path7%
echo ============================================
echo 9. Smoke
echo ============================================
echo 0. Назад
echo ============================================

:: Ожидание нажатия клавиши
choice /c 012345679 /n >nul

:: Проверка выбранного варианта
if errorlevel 1 if not errorlevel 2 goto :selectProduct
if errorlevel 2 set "newPath=%path1%" & set "section=1. %path1%"
if errorlevel 3 set "newPath=%path2%" & set "section=2. %path2%"
if errorlevel 4 set "newPath=%path3%" & set "section=3. %path3%"
if errorlevel 5 set "newPath=%path4%" & set "section=4. %path4%"
if errorlevel 6 set "newPath=%path5%" & set "section=5. %path5%"
if errorlevel 7 set "newPath=%path6%" & set "section=6. %path6%"
if errorlevel 8 set "newPath=%path7%" & set "section=7. %path7%"
if errorlevel 9 set "newPath=%path9%" & set "section=9. %path9%"

:: Проверка, что переменная newPath установлена
if not defined newPath (
    color %COLOR_ERROR%
    echo Ошибка: Неверный выбор раздела тестирования.
    pause
    color %COLOR_RESET%
    goto :menu
)

:: Формирование имени файла
set "fileName=C:\github\VAFitness\bat\Sample_%productType%.json"

:: Чтение исходного файла и замена слова TestPathPlaceholder на выбранный путь
(for /f "delims=" %%i in (%fileName%) do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    echo !line:TestPathPlaceholder=%newPath%!>>VAParams.json
    endlocal
))

cls
color %COLOR_MENU%
echo ============================================
echo   Вы подтверждаете запуск тестов для:
echo   Продукт: %productType%
echo   Раздел: %section%
echo ============================================
echo Нажмите 0 для возврата в меню.
echo Нажмите 1 для продолжения.
echo ============================================

:: Ожидание нажатия клавиши
choice /c 01 /n >nul

:: Проверка нажатой клавиши
if errorlevel 1 if not errorlevel 2 goto :menu
color %COLOR_RESET%

:: Очистка содержимого каталога C:\VA_test\allure\results
echo Очистка содержимого каталога C:\VA_test\allure\results...

if exist "C:\VA_test\allure\results" (
    del /q "C:\VA_test\allure\results\*" >nul
    for /d %%D in ("C:\VA_test\allure\results\*") do rmdir /s /q "%%D"
)

:: Создание пустого каталога (если необходимо)
if not exist "C:\VA_test\allure\results" (
    mkdir "C:\VA_test\allure\results"
)

:: Запуск внешних команд с учетом выбранной базы данных
"C:\Program Files (x86)\1cv8\8.3.24.1368\bin\1cv8c" /N"Админ" /TestManager /Execute "C:\VA_test\epf\vanessa-automation.epf" /IBConnectionString "Srvr=""DESKTOP-BIF25NH"";Ref=""%dbName%"";" /C"StartFeaturePlayer;QuietInstallVanessaExt;VAParams=C:\github\VAFitness\bat\VAParams.json"
allure generate --clean "C:\VA_test\allure\results" && allure open

:exit
color %COLOR_RESET%
exit /b
