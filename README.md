
Steps after downloading

 - Enter a python venv and install requirements from requirements.txt
 - Run `flask db upgrade` to create the local database
 - Run `create_defaults.py` to create the default set of users for testing

To run the application

 - Run `python -m smtpd -n -c DebuggingServer localhost:8025` to start a local email server
 - Run `flask run` or `main.py` to start the flask application
