﻿#language: ru

@tree

Функционал: Проверка заполнения первоначальной настройки при обновлении 

Контекст:
	// Нужно ПОМЕНЯТЬ параметры: 'Порт', 'Строка соединения'
	Дано Я подключаю клиент тестирования с параметрами:
		| 'Имя' | 'Синоним' | 'Тип клиента' | 'Порт' | 'Строка соединения'           | 'Логин' | 'Пароль' | 'Запускаемая обработка' | 'Дополнительные параметры строки запуска' |
		| 'udd' | ''        | 'Тонкий'      | ''     | 'Srvr="localhost";Ref="udd";' | ''      | ''       | ''                      | ''                                        |

Сценарий: 01. Проверка заполнения
	И я удаляю все переменные
	// Ждём процесс обновления по заверщению или до 1 часа
	И я жду открытия окна "Первоначальная настройка" в течение 3600 секунд
	И в поле с именем 'ПользовательИмя' я ввожу текст "admin"

	// Часовой пояс
	И я нажимаю на кнопку с именем 'ВремяТекущегоСеанса'
	Тогда открылось окно "1С:Предприятие"
	И я нажимаю на кнопку с именем 'Button0'
	И из выпадающего списка с именем 'ЧасовойПоясПрограммы' я выбираю точное значение "Europe/Chisinau"
	
	// Страна (создание)
	И я нажимаю на кнопку создать поля с именем 'СтранаУчета'
	И в поле с именем 'Наименование' я ввожу текст "Россия"
	И в поле с именем 'НаименованиеПолное' я ввожу текст "Россия"
	И я запоминаю случайное число в диапазоне от "100" до "999" в переменную "КодСтраны"
	И в поле с именем 'Код' я ввожу текст "$КодСтраны$"
	И в поле с именем 'КодАльфа2' я ввожу текст "MD"
	И в поле с именем 'КодАльфа3' я ввожу текст "MDA"
	И я нажимаю на кнопку создать поля с именем 'ВалютаУчета'
	
	// Валютаx
	И я активизирую окно "Валюта (создание)*"
	И в поле с именем 'НаименованиеПолное' я ввожу текст "ru"
	И я запоминаю случайное число в диапазоне от "100" до "999" в переменную "КодВалюты"
	И в поле с именем 'Код' я ввожу текст "$КодВалюты$"
	И в поле с именем 'Наименование' я ввожу текст "L"
	И в поле с именем 'СимвольноеПредставление' я ввожу текст "ISO"
	И я нажимаю на гиперссылку с именем 'ПараметрыПрописиВалюты'
	И из выпадающего списка с именем 'ПолеПрописи4наРусском' я выбираю точное значение "Мужской"
	И в поле с именем 'ПолеПрописи1наРусском' я ввожу текст "Лей"
	И в поле с именем 'ПолеПрописи2наРусском' я ввожу текст "Лея"
	И в поле с именем 'ПолеПрописи3наРусском' я ввожу текст "Лей"
	И из выпадающего списка с именем 'ПолеПрописи8наРусском' я выбираю точное значение "Мужской"
	И в поле с именем 'ПолеПрописи5наРусском' я ввожу текст "Лей"
	И в поле с именем 'ПолеПрописи6наРусском' я ввожу текст "Лея"
	И в поле с именем 'ПолеПрописи7наРусском' я ввожу текст "Лей"
	И я нажимаю на кнопку с именем 'ФормаУстановить'
	И я нажимаю на кнопку с именем 'ФормаКнопкаСохранитьИЗакрыть'
	
	// Страна (продолжение)
	И в поле с именем 'ТелефонныйКод' я ввожу текст "373"
	И я нажимаю на кнопку с именем 'ФормаКнопкаСохранитьИЗакрыть'

	// Название клуба
	И в поле с именем 'НазваниеФитнесЦентра' я ввожу текст "ФитнесБобёр"
	
	// Ставка НДС
	И из выпадающего списка с именем 'СтавкаНДС' я выбираю точное значение "Без НДС"

	// График работы клуба
	И из выпадающего списка с именем 'ВремяНачалаРаботы' я выбираю точное значение "06:00"
	И из выпадающего списка с именем 'ВремяОкончанияРаботы' я выбираю точное значение "22:00"

	// Проверка тумблера "перепродажи"
	//И я устанавливаю флаг с именем 'ПредпродажаДоОткрытияКлуба'
//	И в поле с именем 'ЗапланированнаяДатаОткрытияКлуба' я ввожу текст "$$Сегодня$$"
	//И в поле с именем 'ДатаАктивацииПредварительныхПродаж' я ввожу текст "$$Завтра$$"
	

	// --- DANGER DANGER DANGER --- ОСТОРОЖНО СОХРАНЕНИЕ :)
	И я нажимаю на кнопку с именем 'Вперед'	
		
	
		

		