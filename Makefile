install:
	poetry install

run:
	poetry run python manage.py runserver

req:
	poetry export -f requirements.txt --output requirements.txt

deps:
	poetry update

deploy:
	git push heroku main
