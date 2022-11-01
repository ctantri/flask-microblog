# Flask Microblog

The microblog web app is the overarching project of the _Flask Mega-Tutorial_ by Miguel Grinberg. The end product can be found at https://github.com/miguelgrinberg/microblog. 

I am following the tutorial from scratch in this repository, though unlike the tutorial I am using [Poetry](https://python-poetry.org/) for package management.

## Initial setup

1. Install using `poetry install`.
2. Create a .flaskenv file containing the line `FLASK_APP=microblog.py`.
3. Create the SQLite database file using `flask db upgrade`.

## How to run
1. Update the database using `flask db upgrade` after each pull from origin.
2. To run the app server, use `flask run`.