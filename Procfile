release: python manage.py migrate
web: gunicorn --chdir Social_Website_New manage.py:app 
$heroku ps:scale web=1
