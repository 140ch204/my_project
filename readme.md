# Django Installation for Heroku

https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

https://learndjango.com/tutorials/django-login-and-logout-tutorial
https://learndjango.com/tutorials/django-login-and-logout-tutorial

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

python manage.py collectstatic
python manage.py runserver

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
heroku config

heroku run python manage.py shell

heroku run bash
    python manage.py migrate
    python manage.py createsuperuser


heroku pg:info
heroku pg:psql
    \l;
    \dt;
    SELECT * FROM auth_user;



python manage.py shell

from django.contrib.auth.models import User
User.objects.all()

super user local : 
login: joe
mdp: admin
email: joe@example.com

login: john
email: lennon@thebeatles.com
mdp: johnpassword


