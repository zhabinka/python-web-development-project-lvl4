install:
	poetry install

run:
	poetry run python manage.py runserver

req:
	pip3 freeze > requirements.txt
