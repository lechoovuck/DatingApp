# DatingApp
<details>

<summary>Русский</summary>

## Установка зависимостей

1. Убедитесь, что на вашей системе установлен Python версии 3.10 или выше.
2. Клонируйте репозиторий проекта на вашу локальную машину.
3. В терминале перейдите в директорию проекта.
4. Создайте виртуальное окружение, чтобы изолировать зависимости проекта:
`python -m venv myenv`

5. Активируйте виртуальное окружение:

- Для Windows:

  `myenv\Scripts\activate`

- Для macOS/Linux:

  `source myenv/bin/activate`

6. Установите зависимости из файла `requirements.txt`:

`pip install -r requirements.txt`

## Конфигурация базы данных

1. Откройте файл `settings.py` в директории проекта.
2. Найдите секцию `DATABASES` и настройте соединение с вашей базой данных. Вы можете использовать SQLite, MySQL, PostgreSQL или другую базу данных, поддерживаемую Django.
3. Раскомментируйте необходимые параметры, такие как имя базы данных, пользователя, пароль и хост.
4. Сохраните изменения в файле `settings.py`.
5. Создайте файл .env в директории проекта.
6. Аналогично файлу `.env-dist` создайте переменные окружения и сохраните этот файл.

## Применение миграций

1. В терминале перейдите в директорию проекта.
2. Выполните следующую команду для создания необходимых таблиц в базе данных:
`python manage.py makemigrations`
`python manage.py migrate`


## Запуск сервера разработки

1. В терминале перейдите в директорию проекта.
2. Запустите сервер разработки Django с помощью следующей команды:
`python manage.py runserver`


3. После успешного запуска сервера, откройте веб-браузер и перейдите по адресу `http://localhost:8000/` для доступа к вашему проекту на Django.

## Дополнительные шаги

- Для настройки статических файлов и медиа-файлов, обратитесь к соответствующей документации Django.
- Для создания суперпользователя (администратора), используйте следующую команду:
`python manage.py createsuperuser`
Следуйте инструкциям в терминале для указания имени пользователя и пароля.

</details>

<details>

<summary>English</summary>

## Installing dependencies

1. Make sure you have Python version 3.10 or higher installed on your system.
2. Clone the project repository to your local machine.
3. In the terminal, navigate to the project directory.
4. Create a virtual environment to isolate the project's dependencies:
`python -m venv myenv`.

5. Activate the virtual environment:

- For Windows:

  `myenv\Scripts\activate`.

- For macOS/Linux:

  `source myenv/bin/activate`.

6. Install dependencies from the `requirements.txt` file:

`pip install -r requirements.txt`.

## Database Configuration

1. Open the `settings.py` file in the project directory.
2. Locate the `DATABASES` section and configure a connection to your database. You can use SQLite, MySQL, PostgreSQL or another database supported by Django.
3. Uncomment the required parameters such as database name, user, password and host.
4. Save the changes in the `settings.py` file.
5. Create an .env file in the project directory.
6. Similar to the `.env-dist` file, create environment variables and save this file.

## Applying migrations

1. In the terminal, navigate to the project directory.
2. Run the following command to create the necessary tables in the database:
`python manage.py makemigrations`.
`python manage.py migrate`.


## Start the development server

1. In the terminal, navigate to the project directory.
2. Start the Django development server using the following command:
`python manage.py runserver`.


3. Once the server is successfully started, open a web browser and navigate to `http://localhost:8000/` to access your Django project.

## Additional steps

- To configure static files and media files, refer to the appropriate Django documentation.
- To create a superuser (administrator), use the following command:
`python manage.py createsuperuser`.
Follow the instructions in the terminal to specify a username and password.

</details>


