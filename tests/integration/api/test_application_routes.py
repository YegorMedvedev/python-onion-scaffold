import unittest
# import src.app as app

from src.app.test_base import BaseTestCase


class TestApplicationRoutes(BaseTestCase):
    def setUp(self):
        app.create_app()
        self.client = app.app.test_client()

    def test_health(self):
        response = self.client.get('/application/health')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()