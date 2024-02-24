

Django app with htmx based on PDCA cycle

- enter kpis
- enter glide
- enter real kpi values
- enter activities based on kpis
  
## PDCA приложение на Django

**Описание**

Это приложение на Django, в котором можно вводить таргеты и цели по kpi ( P part of PDCA Cycle ) 

**Ссылка на GitHub:** [https://github.com/DonnyHipp/django-pdca_app/](https://github.com/DonnyHipp/django-pdca_app/)

**Функциональность**

* **Планирование:**
    * Создание планов с этапами, задачами и сроками.
    * Назначение задач пользователям.
* **Выполнение:**
    * Отслеживание выполнения задач.
    * Добавление комментариев к задачам.
* **Проверка:**
    * Отслеживание прогресса планов.
    * Сравнение фактических результатов с запланированными.
* **Действие:**
    * Внесение корректировок в планы и задачи.
    * Анализ причин отклонений от запланированных результатов.

**Технологии**

* Django >3.2
* Python 3.9
* PostgreSQL

**Установка**

1. Скачайте код из GitHub:

```
git clone https://github.com/DonnyHipp/django-pdca_app.git
```

2. Создайте виртуальное окружение и активируйте его:

```
poetry install 
poetry run python3 maange.py runserver
```


4. Создайте файл `settings.py` и укажите в нем параметры подключения к базе данных:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pdca',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Синхронизируйте модель с базой данных:

```
python manage.py makemigrations
python manage.py migrate
```

6. Запустите сервер:

```
python manage.py runserver
```

**Использование**

1. Зайдите в админку Django: http://127.0.0.1:8000/admin/
3. Создайте kpi, создайте отделы, создайте конфигурации и вводи значения.


**Лицензия**

MIT

