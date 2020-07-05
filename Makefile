FLASK_APP = book_app
# FLASK_ENV := development
FLASK_DEBUG := 1
FLASK_RUN_PORT := 5000

export FLASK_APP
export FLASK_RUN_PORT
export FLASK_DEBUG

dev:
	flask run

prod:
	waitress-serve --port=5000 --call 'book_app:create_app' & disown