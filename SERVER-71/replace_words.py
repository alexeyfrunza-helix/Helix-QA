import sys
TestPathPlaceholder = sys.argv[1]
allureResultsDir = sys.argv[2]
workSpaceDir = sys.argv[3]
sourceFile = sys.argv[4]
vaParamsjson = sys.argv[5]

params = {
    'TestPathPlaceholder': TestPathPlaceholder,
    'workSpaceDir': workSpaceDir,
    'allureResultsDir': allureResultsDir
}

# Чтение исходного файла и замена слов
with open(sourceFile, 'r', encoding='utf-8') as infile, open(vaParamsjson, 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.replace('TestPathPlaceholder', params['TestPathPlaceholder'])
        line = line.replace('workSpaceDir', params['workSpaceDir'])
        line = line.replace('allureResultsDir', params['allureResultsDir'])
        outfile.write(line)

print(f'Обработка завершена. Результат сохранен в {vaParamsjson}')


# Собирает VAParams.json в нужный вид с переменными