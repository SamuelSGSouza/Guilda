run:
	python manage.py runserver

venv:
	venv\scripts\activate

reqs:
	pip freeze -r "requirements.txt"