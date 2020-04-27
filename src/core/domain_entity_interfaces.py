from typing import Optional

from pydantic import BaseModel


class PostgresHealth(BaseModel):
    status: str
    latest_migration: Optional[str]


class StorageConnection(BaseModel):
    postgres: PostgresHealth


class ApplicationHealth(BaseModel):
    python: str
    version: str
    name: str
    environment: dict
    storage: StorageConnection


class AlembicVersion(BaseModel):
    version: str
