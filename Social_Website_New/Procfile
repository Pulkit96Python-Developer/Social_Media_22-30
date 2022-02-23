release: python manage.py migrate
web: gunicorn connect2buddy-app.wsgi --log-file=-
$heroku ps:scale web=1
