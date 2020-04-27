# Django Installation for Heroku

https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

## Django Initialization :

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
    web: gunicorn my_project.wsgi --log-file -

touch runtime.txt
    python-3.6.10

pip install gunicorn dj-database-url whitenoise psycopg2

pip freeze > requirements.txt

## Github 

git add .
git commit -m "init"
git push origin master

## Heroku 

git push heroku master

heroku create herokudjangoapp
heroku config:set   DISABLE_COLLECTSTATIC=1 and restarting
heroku run python manage.py migrate
heroku logs --tail
