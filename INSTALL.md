## Для запуска проекта

 - устанавливаем Python 3.9
   
    В зависимости от системы:
     - LINUX - sudo apt install python3.9
     - WINDOWS - https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe

 - устанавливаем/обновляем pip
   
    В зависимости от системы:
     - LINUX - sudo apt-get install -y python3-pip
     - WINDOWS - python -m pip install --upgrade pip

 - установить виртуальное окружение venv

    В зависимости от системы:
     - LINUX - sudo apt-get install python3-venv
     - WINDOWS - в Python 3 уже стоит
     
 - создать виртуальное окружение venv в папке проекта (или где удобно)

    В зависимости от системы:
     - LINUX - python3 -m venv venv
     - WINDOWS - python -m venv venv

 - активировать виртуальное окружение venv

    В зависимости от системы:
     - LINUX - source venv/bin/activate
     - WINDOWS - venv\Scripts\activate.bat

 - установить пакеты из requirements.txt
   
    В зависимости от системы:
     - LINUX - python3 -m pip install -r requirements.txt
     - WINDOWS - pip install -r requirements.txt
    
    Содержимое файла requirements.txt:
     - Django==2.2.10
     - djangorestframework==3.12.4
     - psycopg2-binary==2.9.1
     - PyJWT==2.1.0
     - pytz==2021.1
     - sqlparse==0.4.1
   
 - устанавливаем БД PostgreSQL

    В зависимости от системы:
     - LINUX - sudo apt install postgresql
     - WINDOWS - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
   
 - меняем настройки БД в файле Interview/Interview/settings.py на установленные выше
    
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'mike159753',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
   
 - создать миграции

    python manage.py makemigrations
   
 - провести миграции

    python manage.py migrate
   
 - при необходимости, создать суперпользователя

    python manage.py createsuperuser
   
 - для полноценного развертывания установить и настроить gunicorn и nginx

    Инструкция доступна в оф. документации
   
 - для тестового запуска проекта

    python manage.py runserver
