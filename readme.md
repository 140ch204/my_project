# Django Installation for Heroku

https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4


mkdir projectfolder

cd projectfolder

virtualenv env -p python3

source env/bin/activate

pip install django

django-admin.py startproject my_project

cd my_project

python manage.py startapp herokuapp

python manage.py migrate

python manage.py runserver

touch Procfile
    web: gunicorn djangoherokuapp.wsgi --log-file -

touch runtime.txt
    python-3.6.9