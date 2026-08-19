@echo off

set folder="C:\Users\sakin\Desktop\code\WikipediaPeopleMap\backend\myproject\myapp\migrations"

for %%f in ("%folder%\*") do (
    if /I not "%%~nxf"=="__init__.py" del "%%f"
)

del C:\Users\sakin\Desktop\code\WikipediaPeopleMap\backend\myproject\db.sqlite3

python manage.py makemigrations myapp
python manage.py migrate

python manage.py makemigrations myapp
python manage.py migrate
python manage.py showmigrations

echo Done!