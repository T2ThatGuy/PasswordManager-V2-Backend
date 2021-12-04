
Steps after downloading

 - Enter a python venv and install requirements from requirements.txt
 - Run `flask db upgrade` to create the local database
 - Run `create_defaults.py` to create the default set of users for testing

 - Create a .flaskenv file and add some of the following tags:
    - `FLASK_MODE=[development|production]`
    - `FLASK_APP=main.py`
    - `MAIL_SERVER=[address]` -> defaults to localhost
    - `MAIL_PORT=[port]` -> defaults to 25

To run the application

 - Run `python -m smtpd -n -c DebuggingServer localhost:8025` to start a local email server
 - Run `flask run` or `main.py` to start the flask application
