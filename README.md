# Платформа онлайн-обучения <img width="137" height="41" alt="Skypro" src="https://github.com/user-attachments/assets/ac708293-d4d3-4222-980d-a89643052ae0" />

Бэкенд-часть SPA-приложения для платформы онлайн-обучения, разработанная на **Django** и **Django REST Framework** с использованием JWT-авторизации и разграничения прав доступа.

## Функционал проекта
* **Авторизация и пользователи (`users.User`):**
  * Авторизация по `email` (стандартное поле `username` отключено).
  * JWT-аутентификация на базе `djangorestframework-simplejwt` (`access` и `refresh` токены). Все эндпоинты закрыты по умолчанию (`IsAuthenticated`), кроме регистрации и получения/обновления токена (`AllowAny`).
  * Полный CRUD для пользователей с хешированием пароля при регистрации и выводом истории платежей в профиле.
* **Права доступа и роли (`users.permissions`):**
  * **Модераторы (`IsModer`, группа `moders`):** могут просматривать и редактировать любые курсы и уроки, но не могут создавать новые и удалять существующие. Группа выгружена в фикстуру `users/fixtures/groups.json`.
  * **Владельцы (`IsOwner`):** обычные пользователи при создании курса или урока автоматически назначаются его владельцем (`owner`) и имеют доступ (просмотр, редактирование, удаление) только к собственным материалам.
* **Учебные материалы (`materials`):**
  * **Курсы (`Course`):** полный CRUD через `ModelViewSet` и `DefaultRouter`, вычисляемое поле количества уроков (`lessons_count`) и вложенный список уроков (`lessons`).
  * **Уроки (`Lesson`):** полный CRUD через `Generic`-классы, связь с курсами «один ко многим».
* **Платежи (`users.Payment`):**
  * История оплат курсов и уроков с фильтрацией по курсу, уроку, способу оплаты (`cash` / `transfer`) и сортировкой по дате (`django-filter` и `OrderingFilter`).

## Технологический стек
* Python 3.12+
* Django / Django REST Framework
* djangorestframework-simplejwt (JWT-аутентификация)
* django-filter (фильтрация и сортировка в API)
* Pillow (работа с изображениями и медиафайлами)
* Poetry (управление зависимостями)

## Установка и запуск проекта

1. **Клонируйте репозиторий и перейдите в директорию проекта:**
   ```bash
   # 30.1 клонируем удаленный репозиторий на локальный компьютер
   git clone <ссылка_на_ваш_репозиторий>
   cd 31_Django_DZ
   ```

2. **Установите зависимости через Poetry:**
   ```bash
   # 31 устанавливаем все зависимости проекта (включая djangorestframework-simplejwt)
   poetry install
   ```

3. **Примените миграции базы данных:**
   ```bash
   # 31 создаем и обновляем таблицы в базе данных
   poetry run python manage.py migrate
   ```

4. **Загрузите фикстуру группы модераторов и тестовые платежи:**
   ```bash
   # 31 загружаем группу модераторов moders из фикстуры
   poetry run python manage.py loaddata users/fixtures/groups.json

   # 30.2 наполняем базу тестовыми курсами, уроками и платежами (на выбор)
   poetry run python manage.py fill_payments
   ```

5. **Создайте суперпользователя (при необходимости):**
   ```bash
   # 30.1 создаем учетную запись администратора (логин вводится в формате email)
   poetry run python manage.py createsuperuser
   ```

6. **Запустите локальный сервер разработки:**
   ```bash
   # 30.1 запускаем тестовый веб-сервер Django
   poetry run python manage.py runserver
   ```

## Основные эндпоинты API

### Авторизация и пользователи (`AllowAny` / `IsAuthenticated`)
* `POST /register/` — регистрация нового пользователя (`AllowAny`)
* `POST /login/` — получение пары `access` и `refresh` JWT-токенов (`AllowAny`)
* `POST /token/refresh/` — обновление `access`-токена по `refresh`-токену (`AllowAny`)
* `GET /users/` — список всех пользователей
* `GET /users/<id>/` — просмотр профиля пользователя (включая историю платежей `payments`)
* `PUT / PATCH /users/update/<id>/` — редактирование профиля пользователя
* `DELETE /users/delete/<id>/` — удаление пользователя

### Курсы (`ViewSet` + права `IsModer`, `IsOwner`)
* `GET /courses/` — список курсов (модераторам — все, пользователям — только свои)
* `POST /courses/` — создание курса с автопривязкой `owner` (запрещено модераторам)
* `GET /courses/<id>/` — детальный просмотр курса (модератор или владелец)
* `PUT / PATCH /courses/<id>/` — редактирование курса (модератор или владелец)
* `DELETE /courses/<id>/` — удаление курса (только владелец, запрещено модераторам)

### Уроки (`Generic`-классы + права `IsModer`, `IsOwner`)
* `POST /lessons/create/` — создание урока с автопривязкой `owner` (запрещено модераторам)
* `GET /lessons/` — список уроков (модераторам — все, пользователям — только свои)
* `GET /lessons/<id>/` — детальный просмотр урока (модератор или владелец)
* `PUT / PATCH /lessons/update/<id>/` — редактирование урока (модератор или владелец)
* `DELETE /lessons/delete/<id>/` — удаление урока (только владелец, запрещено модераторам)

### Платежи (`Generic`-классы + `django-filter`)
* `GET /payments/` — список платежей с поддержкой фильтрации (`?payment_method=`, `?paid_course=`, `?paid_lesson=`) и сортировки (`?ordering=payment_date`, `?ordering=-payment_date`)


* Главная страница: [http://127.0.0.1:8000/](http://127.0.0)
* Административная панель Django: [http://127.0.0.1:8000/admin/](http://127.0.0admin/)

## Структура проекта

```text 

30-2_Django_DZ/                     # 30.2 Корневая директория проекта (платформа онлайн-обучения на DRF)
│
├── config/                         # 30.1 Главная конфигурационная папка проекта Django
│   ├── __init__.py                 # 30.1 Инициализация пакета конфигурации проекта
│   ├── asgi.py                     # 30.1 Асинхронный интерфейс веб-сервера
│   ├── settings.py                 # 30.2 Главные настройки проекта (DRF, django_filters, AUTH_USER_MODEL, MEDIA)
│   ├── urls.py                     # 30.1 Главный файл маршрутизации (пути admin, приложений materials и users, медиафайлы)
│   └── wsgi.py                     # 30.1 Синхронный интерфейс веб-сервера
│
├── materials/                      # 30.1 Приложение «Учебные материалы» (Курсы и уроки)
│   ├── migrations/                 # 30.1 Папка миграций приложения в базе данных
│   │   ├── 0001_initial.py         # 30.1 Создание таблиц Course и Lesson с внешним ключом на курс
│   │   └── __init__.py             # 30.1 Инициализация пакета миграций
│   ├── __init__.py                 # 30.1 Инициализация пакета приложения materials
│   ├── admin.py                    # 30.1 Регистрация моделей Course и Lesson в панели администратора
│   ├── apps.py                     # 30.1 Конфигурация приложения materials
│   ├── models.py                   # 30.1 Модели БД: Course (название, превью, описание) и Lesson (связь с курсом, видео)
│   ├── serializers.py              # 30.2 Сериализаторы DRF: LessonSerializer и CourseSerializer (с lessons_count и вложенным списком уроков)
│   ├── tests.py                    # 30.1 Модуль для написания автотестов приложения
│   ├── urls.py                     # 30.1 Маршруты API (DefaultRouter для курсов и path для Generic-уроков)
│   └── views.py                    # 30.1 Контроллеры API: CourseViewSet (ModelViewSet) и Generic-классы для Lesson
│
├── users/                          # 30.1 Приложение «Пользователи» (Кастомная модель, профиль и платежи)
│   ├── management/                 # 30.2 Пакет для пользовательских management-команд Django
│   │   ├── commands/               # 30.2 Директория кастомных консольных команд приложения users
│   │   │   ├── __init__.py         # 30.2 Инициализация пакета команд
│   │   │   └── fill_payments.py    # 30.2 Кастомная команда для наполнения БД тестовыми курсами, уроками и платежами
│   │   └── __init__.py             # 30.2 Инициализация пакета management
│   ├── migrations/                 # 30.1 Папка миграций пользователей в базе данных
│   │   ├── 0001_initial.py         # 30.1 Создание кастомной таблицы User с авторизацией по email
│   │   ├── 0002_payment.py         # 30.2 Создание таблицы Payment (связь с User, Course, Lesson, сумма, способ оплаты)
│   │   └── __init__.py             # 30.1 Инициализация пакета миграций
│   ├── __init__.py                 # 30.1 Инициализация пакета приложения users
│   ├── admin.py                    # 30.2 Регистрация моделей User и Payment в административной панели Django
│   ├── apps.py                     # 30.1 Конфигурация приложения users
│   ├── models.py                   # 30.2 Модели User (вход по email, phone, city, avatar) и Payment (история оплат)
│   ├── serializers.py              # 30.2 Сериализаторы PaymentSerializer и UserSerializer (с историей платежей пользователя)
│   ├── tests.py                    # 30.1 Модуль для написания автотестов пользователей
│   ├── urls.py                     # 30.2 Маршруты API для профиля пользователя и списка платежей с фильтрацией
│   └── views.py                    # 30.2 Контроллеры API: UserUpdateAPIView и PaymentListAPIView (с фильтрацией и сортировкой)
│
├── media/                          # 30.1 Динамическая папка проекта (Загружаемые медиафайлы)
│   ├── materials/                  # 30.1 Изображения учебных материалов
│   │   ├── courses/
│   │   │   └── previews/           # 30.1 Загруженные превью-обложки курсов
│   │   └── lessons/
│   │       └── previews/           # 30.1 Загруженные превью-обложки уроков
│   └── users/
│       └── avatars/                # 30.1 Загруженные пользователями аватарки
│
├── .gitignore                      # 30.1 Список файлов и папок, игнорируемых системой Git (venv, media, db.sqlite3, .env)
├── manage.py                       # 30.1 Главный управляющий скрипт Django-проекта
├── payments_fixture.json           # 30.2 Фикстура с выгруженными тестовыми данными модели Payment
├── pyproject.toml                  # 30.2 Конфигурационный файл Poetry со списком зависимостей (Django, DRF, Pillow, django-filter)
├── poetry.lock                     # 30.2 Зафиксированные версии установленных библиотек Poetry
└── README.md                       # 30.2 Документация проекта и инструкция по запуску для проверки ДЗ
```
### Основные команды
#### 30.1 инициализируем новый проект Poetry в текущей директории (если pyproject.toml еще не создан)
poetry init -n

#### 30.1 устанавливаем Django, Django REST Framework и библиотеку Pillow через Poetry
poetry add django djangorestframework pillow

#### 30.1 создаем новый Django-проект с именем config внутри виртуального окружения Poetry
poetry run django-admin startproject config .

#### 30.1 создаем приложение users для модели кастомного пользователя
poetry run python manage.py startapp users

#### 30.1 создаем приложение materials для моделей курса и урока
poetry run python manage.py startapp materials

#### 30.1 запускаем тестовый сервер Django через Poetry для проверки работоспособности проекта
poetry run python manage.py runserver

#### 30.1 генерируем файлы миграций для созданных моделей в приложениях users и materials
poetry run python manage.py makemigrations

#### 30.1 применяем все миграции и создаем таблицы в базе данных
poetry run python manage.py migrate

#### 30.2 запускаем кастомную команду для наполнения таблицы платежей тестовыми данными
poetry run python manage.py fill_payments

#### 30.2 выгружаем данные платежей напрямую в файл payments_fixture.json
poetry run python -Xutf8 manage.py dumpdata users.Payment --indent 2 -o payments_fixture.json

#### 30.2 устанавливаем библиотеку django-filter через Poetry для фильтрации и сортировки в DRF
poetry add django-filter

#### 31 устанавливаем библиотеку djangorestframework-simplejwt для работы с JWT-токенами
poetry add djangorestframework-simplejwt

#### 31 создаем директорию fixtures внутри приложения users
mkdir users\fixtures

#### 31 выгружаем группы пользователей в fixtures
poetry run python -Xutf8 manage.py dumpdata auth.group --indent 2 -o users/fixtures/groups.json
