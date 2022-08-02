# API YaMDB

Проект предназначен для обмена мнениями о произведениях искусства и выставления им рейтинга:

- интерфейс реализован через REST API;
- есть регистрация и авторизация пользователей;
- добавление и удаление обзоров на произведения;
- выставление и изменение рейтинга;
- расчёт средней оценки произведения по обзорам;
- добавление, редактирование и удаление комментариев под обзорами;
- произведения разделены по категориями: кино, музыка, книги; и по жанрам;
- разделение ролей на пользователей, модераторов и администраторов;
- модераторы и администраторы могут добавлять произведения, новые жанры и новые категории.

## Применяемые технологии:

- Python 3.9.6
- Django 2,2,16
- Django Rest Framework 3,12,4
- Simple JWT 4,7,2
- SQLite 3

## Как запустить проект:

**На Windows:**

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

## Документация
После запуска автономного сервера документация API расположена по ардесу:

http://127.0.0.1:8000/redoc/

## Примеры запросов:

### Регистрация нового пользователя и получение токена:
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

### Получение списка всех произведений:
**GET** /api/v1/titles/

*Ответ в случае пустой базы:*
``` 
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
``` 

*или вид ответа в случае наличия записей:*
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

## Авторы:

- Козлов Павел -- система управления пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail;
- Отаров Александр -- отзывы (Review) и комментарии (Comments): модели, представления, эндпойнты для них, рейтинги произведений;
- Черваков Дмитрий -- категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них.
