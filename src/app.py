from os import getenv

from api import application_routes
from flask import Flask
from infrastructure.database.connection import DatabaseConnection
from infrastructure.utils.config import read_env_config
from infrastructure.utils.exceptions import error_handler

app = Flask(__name__)
database = DatabaseConnection()


def before_all():
    read_env_config()
    database.establish_connection()
    database.create_session()
    database.generate_database_schema()


def init_application():
    app.register_blueprint(application_routes.http)
    app.register_error_handler(Exception, error_handler)
    app.run(port=getenv("PORT"))


if __name__ == '__main__':
    before_all()
    init_application()
