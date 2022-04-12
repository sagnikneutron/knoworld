import os 
os.system('rm db.sqlite3')
os.system('python3 manage.py makemigrations')
os.system('python3 manage.py migrate')
os.system('python3 manage.py runserver ')

