"web: gunicorn mysite.wsgi --log-file -" 
release:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb