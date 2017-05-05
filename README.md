# ITC Backend

## Adding entries

The process is simple. Doing this ensures backups so if something gets messed up, we do not lose data.

First, run `git pull` to get the latest stuff.

1. On local, open a terminal

2. Run `python manage.py dumpdata --exclude auth.permission --exclude contenttype --exclude corsheaders > data.json`. This exports the server to a JSON file. This is the backup of the server. The server can be restored from this file.

3. Move this file to `db_backups` and rename it with the current date (and time preferably).

4. Run `python manage.py runserver` to start a server locally.

5. Open a browser and go to `localhost:8000`. This is the server's API. This is where you will add the results/splits/news/any additions.

6. Add entries/news/whatever through the browser.

7. Spin up a local instance of the frontend to test anything to make sure the changes are working. You'll need to point the frontend at `localhost:8000` instead of at Heroku.

8. Once everything looks good, shut off the server (`CTRL-C`) and the frontend if you spun that up.

9. Now you need to dump out the updated server again. Run `python manage.py dumpdata --exclude auth.permission --exclude contenttype --exclude corsheaders > data.json` again. Keep that there, but make a copy, rename it with date and time, and put it in the `db_backups` folders.

10. Run `git status` to make sure only the files you changed show up. If you run a migration, there will be a weirdly titled migration file. You will need that.

11. Run `git add .`, then `git commit -m "Some message detailing what you do"`, then `git push` to push it up to GitHub.

12. The changes are now committed and backed up. Now you need to update the Heroku server.

13. Run `git push heroku master`. This updates the code on the server. You need to update the db separately still.

14. Login to the Heroku server using `heroku run bash`. This opens a terminal on the server.

15. Run `python manage.py loaddata data.json`. This updates the database to reflect your local changes.

16. Boom. Done. `CTRL-C` out of the Heroku server. Make sure the site works by looking at `illinoistrackclub.com`.


## Dev stuff

Everything below is for changing the server itself in some manner, not just adding entries. Be careful here. Make sure any changes run as expeced on local before pushing to heroku.

## Dev dependencies
* Python 3.5.2
* Django 1.9.7

Install these then run `pip install -r requirements.txt` in this directory from a terminal

## Local development

The local database differs from the Heroku DB. Make sure any local changes compile before pushing to Heroku. The local DB points to db.sqllite3

### Run the server
    python manage.py runserver

### After changes to models
    python manage.py makemigrations
    python manage.py migrate

## Working with Heroku

Hosted at `http://illinoistrackclub.herokuapp.com/`

### Updating Heroku after updating a model locally
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
