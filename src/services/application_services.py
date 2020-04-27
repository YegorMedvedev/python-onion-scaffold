import os
import sys

import infrastructure.database.repositories as repository
import src.core.domain_entity_interfaces as interfaces
from src.version import __version__


def get_application_health() -> interfaces.ApplicationHealth:
    application_repository = repository.ApplicationRepository()

    alembic_version = application_repository.select_latest_migration()
    if alembic_version is None:
        postgres = interfaces.PostgresHealth(
            status="ok",
            latest_migration=None
        )
    else:
        postgres = interfaces.PostgresHealth(
            status="ok",
            latest_migration=alembic_version.dict()["version"]
        )

    storage_connection = interfaces.StorageConnection(
        postgres=postgres
    )

    application_health = interfaces.ApplicationHealth(
        python=sys.version,
        version=__version__,
        name=os.getenv("NAME"),
        environment=os.environ,
        storage=storage_connection
    )

    return application_health
