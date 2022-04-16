Клонировать репозиторий
git clone https://github.com/kirma133113/api_yamdb.git

cd api_yamdb

Cоздать и активировать виртуальное окружение:
python -m venv venv

source venv/scripts/activate

python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python manage.py runserver

В проекте доступны следующие эндпоинты:
http://127.0.0.1:8000/api/v1/auth/signup/  - Получение кода подверждения на email

{
"email": "string",
"username": "string"
}

http://127.0.0.1:8000/api/v1/auth/token/ - Получение токена для авторизации

{
"username": "string",
"confirmation_code": "string"
}

http://127.0.0.1:8000/api/v1/categories/ - Работа с категориями, доступны запросы Get, Post и Del

http://127.0.0.1:8000/api/v1/genres/ - Работа с жанрами, доступны запросы Get, Post и Del

http://127.0.0.1:8000/api/v1/titles/ - Работа со статьями , доступны запросы Get, Post, Patch и Del

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/  - Работа с отзывами , доступны запросы Get, Post, Patch и Del

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Работа с комментариями , доступны запросы Get, Post, Patch и Del

http://127.0.0.1:8000/api/v1/users/ - Создание пользователя и получение информации о всех пользователях. Доступны запросы Get, Post

http://127.0.0.1:8000/api/v1/users/{username}/ - Получение информации о конкретном пользователе и редактирование информации о нем. Доступны доступны запросы Get, Postm Del

http://127.0.0.1:8000/api/v1/users/me/ - Получение и изменение своих данных, доступны запросы Get, Patch

Клонирование базы

прейти в Python Shell командой

python manage.py shell

импорт необходимых модулей

import os
inport csv

установить путь до базы

path = "с:/../api_yamdb/static/data"

Импортировать необходимые модели

from reviews.models import Genre, Category, Title, Review, Comment, GenreTitle
from users.models import User

Последовательно для каждой модели запустить цикл записи данных:

на примере модели пользователей.

with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = User(id=row['id'], username=row['username'], email=row['email'], role=row['role'], bio=row['bio'], first_name=row['first_name'], last_name=row['last_name'])
        p.save()

полный набор команд в файле import_db