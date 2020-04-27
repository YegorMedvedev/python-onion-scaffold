import app

from sqlalchemy import Column, CHAR


class AlembicVersion(app.database.base):
    __tablename__ = "alembic_version"
    version_num = Column(CHAR(32), primary_key=True)
