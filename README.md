# Платформа онлайн-обучения <img width="137" height="41" alt="Skypro" src="https://github.com/user-attachments/assets/ac708293-d4d3-4222-980d-a89643052ae0" />

Бэкенд-часть SPA-приложения для платформы онлайн-обучения, разработанная на **Django** и **Django REST Framework**.

## Функционал проекта
* **Кастомная модель пользователя (`users.User`):**
  * Авторизация по `email` (стандартное поле `username` отключено).
  * Дополнительные поля профиля: `phone`, `city`, `avatar`.
  * Просмотр и редактирование профиля любого пользователя через `RetrieveUpdateAPIView` с выводом истории его платежей (дополнительное задание).
* **Учебные материалы (`materials`):**
  * **Курсы (`Course`):** полный CRUD реализован через `ModelViewSet` и роутер `DefaultRouter`. Сериализатор включает вычисляемое поле количества уроков (`lessons_count`) и вложенный список всех связанных уроков (`lessons`).
  * **Уроки (`Lesson`):** полный CRUD реализован через `Generic`-классы (`CreateAPIView`, `ListAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`), связь с курсами «один ко многим».
* **Платежи (`users.Payment`):**
  * Хранение истории оплат курсов и отдельных уроков с указанием пользователя, даты, суммы и способа оплаты (`cash` / `transfer`).
  * Фильтрация списка платежей по курсу, уроку и способу оплаты, а также сортировка по дате оплаты с помощью `django-filter` и `OrderingFilter`.
  * Наполнение базы данных реализовано через кастомную команду `fill_payments` и фикстуру `payments_fixture.json`.

## Технологический стек
* Python 3.12+
* Django
* Django REST Framework
* django-filter (фильтрация и сортировка в API)
* Pillow (работа с изображениями и медиафайлами)
* Poetry (управление зависимостями и виртуальным окружением)

## Установка и запуск проекта

1. **Клонируйте репозиторий и перейдите в директорию проекта:**
   ```bash
   # 30.1 клонируем удаленный репозиторий на локальный компьютер
   git clone <ссылка_на_ваш_репозиторий>
   cd 30-1_Django_DZ
   ```

2. **Установите зависимости через Poetry:**
   ```bash
   # 30.2 устанавливаем все зависимости проекта (включая django-filter) из pyproject.toml
   poetry install
   ```

3. **Примените миграции базы данных:**
   ```bash
   # 30.2 создаем таблицы в базе данных на основе миграций проекта
   poetry run python manage.py migrate
   ```

4. **Заполните базу данных тестовыми платежами (на выбор):**
   ```bash
   # 30.2 вариант 1: запуск кастомной команды для создания курсов, уроков и платежей
   poetry run python manage.py fill_payments

   # 30.2 вариант 2: загрузка данных из готовой фикстуры
   poetry run python manage.py loaddata payments_fixture.json
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

### Курсы (`ViewSet` + `DefaultRouter`)
* `GET /courses/` — получение списка всех курсов (включая `lessons_count` и вложенный список `lessons`)
* `POST /courses/` — создание нового курса
* `GET /courses/<id>/` — получение детальной информации о курсе
* `PUT / PATCH /courses/<id>/` — полное или частичное обновление курса
* `DELETE /courses/<id>/` — удаление курса

### Уроки (`Generic`-классы)
* `POST /lessons/create/` — создание нового урока
* `GET /lessons/` — получение списка всех уроков
* `GET /lessons/<id>/` — получение детальной информации об уроке
* `PUT / PATCH /lessons/update/<id>/` — полное или частичное обновление урока
* `DELETE /lessons/delete/<id>/` — удаление урока

### Пользователи и платежи (`Generic`-классы + `django-filter`)
* `GET /users/<id>/` — просмотр профиля пользователя (включая историю его платежей `payments`)
* `PUT / PATCH /users/<id>/` — редактирование профиля пользователя
* `GET /payments/` — получение списка платежей с поддержкой параметров фильтрации и сортировки:
  * `?payment_method=cash` или `?payment_method=transfer` — фильтрация по способу оплаты
  * `?paid_course=<id>` — фильтрация по ID оплаченного курса
  * `?paid_lesson=<id>` — фильтрация по ID оплаченного урока
  * `?ordering=payment_date` или `?ordering=-payment_date` — сортировка по дате оплаты

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
