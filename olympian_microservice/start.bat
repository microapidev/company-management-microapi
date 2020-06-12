@ECHO OFF
start cmd.exe /C "docker-compose run web python manage.py migrate && docker-compose build && docker-compose up"
timeout 10
explorer "http://127.0.0.1:8000/"
