# SberTask
Имплементации задачи от Сбербанка 

Код имплементации находиться в app.py написанный на Python3. После загрузки репозитория на локальный компьютер может потребоваться установка библиотек которые используются в проекте. Для этого требуется открыть терминал и попасть в нужный нам репозиторий(SberTask). Отсюда можно использовать команду: pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy requests(Тут я предпологаю что у вас уже установлен python3, если нет то сперва следует его установить). Это должно установить все используемые библиотеки. Дальше можно запускать файл с помощью команды: python app.py(Нужно скопировать адрес сервера где работает программа, в моем случае это http://127.0.0.1:5000). Для проверки работы API я использовал Postman, который можно скачать по следующей ссылке: https://www.postman.com. Нужно настроить метод на POST и там где написанно Enter request URL вставить адрес вашего сервера и добавить /request(В моем случае http://127.0.0.1:5000/request). Ниже строки где вы вводите адрес нужно выбрать вкладку Headers, в поле Key ввести Content-Type и в строке Value ввести application/json. Дальше переходим на вкладку Body(находиться на том же уровне что и вкладка Headers) выбрать raw и ниже прописать запрос в формате JSON: 
{
 "req", "Название города на английском языке"
}
В заключение надо нажать Send и если все шаги были выполнены правильно то ниже написанного вами запроса появиться результат вашего запроса в формате JSON. 

Описание процесса: 
  Когда вы пишите свой запрос и отправляете его программа сперва создает запрос для внешнего API от OpenWeather(https://openweathermap.org) где по названию города находит температуру этого города в градусах цельсия. Далее программа создает строчку в таблице с названием города и температурой на данный момент в этом городе и id этой строки в базе данных. Результат запросы который выводиться на экран в Postmate это созданная в этом запросе строчка из базы данных. 



Обновление 1.1
Добавил 2 функции для запроса в базу данных.

1) Возращает все строки таблицы. Это можно сделать через Postmate просто поменяв POST на GET. 

2) Функция возращает определенную строку из таблицы которая определяется по id. Для этого нужно в Postmate поменять POST на GET и в URL добавить /<id>(в моем случае это выглядит так: http://127.0.0.1:5000/request/1). 
