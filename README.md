# Лабораторная работа № 1 — Python и Django

Программы выводят приветствие и отбирают студентов по среднему баллу. Также создан проект Django с административной панелью.

## Запуск

Установите Python 3.11 и выполните в PowerShell из папки проекта:

Для сохранения входа при перезапуске используйте один и тот же ключ Django.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:DJANGO_SECRET_KEY = Read-Host "Ключ Django"
.\.venv\Scripts\python.exe src/helloworld.py
.\.venv\Scripts\python.exe src/mygroup.py
.\.venv\Scripts\python.exe src/django_project/manage.py migrate
.\.venv\Scripts\python.exe src/django_project/manage.py createsuperuser
.\.venv\Scripts\python.exe src/django_project/manage.py runserver
```

Откройте http://127.0.0.1:8000/. Административная панель: http://127.0.0.1:8000/admin/.
