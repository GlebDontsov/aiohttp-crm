# aiohttp-crm
API-сервис реализованный c помощью асинхронного веб фреймворк на asyncio Python 3.5.3+ для клиентской и серверной сторон - aiohttp.

## Поддерживает методы:

1. Создание пользователя: POST http://127.0.0.1:8080/add_user
2. Список пользователей: GET http://127.0.0.1:8080/list_users
3. Получение одного пользователя: GET http://127.0.0.1:8080/get_user
4. Swagger UI http://127.0.0.1:8080/docs
5. Swagger json http://127.0.0.1:8080/docs/json


## Запуск бота:
1. Используйте Python 3.10.
2. Склонируйте к себе репозиторий <br/>
`https://github.com/GlebDontsov/aiohttp-crm.git`
3. Установите необходимые библиотеки:  
`pip install -r requirements.txt`
4. Запустите API-сервис:  
`python3 main.py`
