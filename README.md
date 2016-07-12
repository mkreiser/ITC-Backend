# ITC Backend

## Dev dependencies
* Python 3.5.2
* Django 1.9.7

Install these then run `pip install -r requirements.txt`

## Local development

The local database differs from the Heroku DB. Make sure any local changes compile before pushing to Heroku

### Run the server
    python manage.py runserver

### After changes to models
    python manage.py makemigrations
    python manage.py migrate

## Working with Heroku

Hosted at `http://mighty-lowlands-90976.herokuapp.com/`

### Updating Heroku after updating master
    git pull master
    git push heroku master
    heroku run python manage.py migrate

### Enter Heroku instance via bash (normal console)
    heroku run bash

### Enter Heroku instance via python (python console)
    heroku run python manage.py shell

### View server logs
    heroku logs

## Backup server data
    python manage.py dumpdata --exclude=corsheaders > data.json
