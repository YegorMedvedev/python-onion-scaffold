from flask import Flask

from api import application_routes
from infrastructure.database.connection import DatabaseConnection
from infrastructure.utils.config import read_env_config
from infrastructure.utils.exceptions import error_handler
from infrastructure.utils.utils import get_port

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
    app.run(port=get_port())


def create_app():
    before_all()
    init_application()


if __name__ == '__main__':
    create_app()
