from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, Session as SqlSession

from infrastructure.utils.utils import Singleton


class DatabaseConnection(metaclass=Singleton):
    engine: Engine
    session: SqlSession
    base: DeclarativeMeta = declarative_base()

    def establish_connection(self):
        postgresql_url = getenv("POSTGRESQL_URL")
        self.engine = create_engine(postgresql_url)

    def generate_database_schema(self):
        self.base.metadata.create_all(self.engine)

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)
