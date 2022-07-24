# API YaMDB

Проект предназначен для обмена мнения о произведениях искусства и выставления им рейтинга.

## Авторы:

- Козлов Павел
- Отаров Александр (galenfea@gmail.com)
- Черваков Дмитрий

## Применяемые технологии:

- Django 2,2,16
- Django Rest Framework 3,12,4
- Simple JWT 4,7,2
- SQLite 3

## Как запустить проект:

_Клонировать репозиторий и перейти в него в командной строке:_
```
git clone https://github.com/pnpt-corp/api_yamdb.git
cd api_yamdb
```

_Cоздать и активировать виртуальное окружение:_
```
python -m venv venv
source venv/Scripts/activate
```

_Установить зависимости из файла requirements.txt:_
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

_Выполнить миграции и запустить проект:_
```
cd api_yamdb
python manage.py migrate
python manage.py runserver
```

## Примеры запросов:

#### Регистрация нового пользователя и получение токена:
**POST** /api/v1/auth/signup/  
_Request:_
```
{
    "email": "string",
    "username": "string"
}
```
_Response:_
```
{
    "email": "string",
    "username": "string"
}
```
**POST** /api/v1/auth/token/  
_Request:_
``` 
{
    "username": "string",
    "confirmation_code": "string"
}
```
_Response:_
```
{
    "token": "string"
}
```

#### Получение списка всех произведений:
**GET** /api/v1/titles/
``` 
{
    "count": 123,
    "next": "http://127.0.0.1:8000/api/v1/titles/?offset=400&limit=100",
    "previous": "http://127.0.0.1:8000/api/v1/titles/?offset=200&limit=100",
    "results": [
        {}
    ]
}
```

#### Отправка рецензии и оценки:
**POST** /api/v1/titles/{title_id}/reviews/   
_Request:_
```
{
    "text": "string",
    "score": 1
}
```
_Response:_
```
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```