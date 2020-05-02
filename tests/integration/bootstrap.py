import unittest
import src.app as source_app


class Bootstrap(unittest.TestCase):
    def setUp(self):
        source_app.before_all()
        source_app.init_application()

        self.app = source_app.app
        self.client = self.app.test_client()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

    def tearDown(self):
        pass
