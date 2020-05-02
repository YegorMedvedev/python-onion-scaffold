import sys
import unittest
import uuid

import mock

from src.core.domain_entity_interfaces import ApplicationHealth, AlembicVersion
from src.services.application_services import get_application_health
from src.version import __version__


class TestGetApplicationHealth(unittest.TestCase):
    @mock.patch('src.services.application_services.os')
    @mock.patch('infrastructure.database.repositories.ApplicationRepository')
    def test_when_no_migrations_were_executed(self, mock_application_repository, mock_os):
        application_repository = mock_application_repository.return_value
        application_repository.select_latest_migration.return_value = None

        project_name = "project-name"
        env_values = dict({"ENV": "test"})

        mock_os.getenv.return_value = project_name
        mock_os.environ = env_values

        result = get_application_health()

        self.assertTrue(type(result), isinstance(ApplicationHealth, type))
        self.assertEqual(result.dict(), {
            "python": sys.version,
            "version": __version__,
            "name": project_name,
            "environment": {'ENV': "test"},
            "storage": {
                "postgres": {
                    "status": "ok",
                    "latest_migration": None,
                }
            }
        })

    @mock.patch('src.services.application_services.os')
    @mock.patch('infrastructure.database.repositories.ApplicationRepository')
    def test_with_executed_migrations(self, mock_application_repository, mock_os):
        latest_migration_version = str(uuid.uuid4())

        application_repository = mock_application_repository.return_value
        application_repository.select_latest_migration.return_value = AlembicVersion(version=latest_migration_version)

        project_name = "project-name"
        env_values = dict({"ENV": "test"})

        mock_os.getenv.return_value = project_name
        mock_os.environ = env_values

        result = get_application_health()

        self.assertTrue(type(result), isinstance(ApplicationHealth, type))
        self.assertEqual(result.dict(), {
            "python": sys.version,
            "version": __version__,
            "name": project_name,
            "environment": {'ENV': "test"},
            "storage": {
                "postgres": {
                    "status": "ok",
                    "latest_migration": latest_migration_version
                }
            }
        })
