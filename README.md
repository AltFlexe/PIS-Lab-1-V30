# Лабораторная работа 1 — Python и Django

Программа `helloworld.py` выводит приветствие. Программа `mygroup.py` выводит учебный список студентов и отбирает тех, чей средний балл строго выше введённого значения. Проект Django содержит стандартную административную панель для управления пользователями.

## Запуск

Требуется Python 3.11. Из корня проекта в PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/helloworld.py
.\.venv\Scripts\python.exe src/mygroup.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe src/django_project/manage.py migrate
.\.venv\Scripts\python.exe src/django_project/manage.py createsuperuser
.\.venv\Scripts\python.exe src/django_project/manage.py runserver
```

Сайт доступен по адресу `http://127.0.0.1:8000/`, административная панель — `/admin/`. Через панель можно создать других пользователей и изменить их права. Учётные записи создаются локально; их пароли и база не входят в репозиторий.

Для локального запуска Django использует переменную окружения `DJANGO_SECRET_KEY`, а если она не задана, создаёт новый случайный ключ при запуске. Из-за этого после перезапуска сервера может потребоваться повторный вход. Такой режим предназначен только для учебной разработки.

`src/` содержит программы и проект Django, `tests/` — проверки программ, `requirements.txt` — зависимости.
