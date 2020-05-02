from tests.integration.bootstrap import Bootstrap


class TestApplicationRoutes(Bootstrap):
    def test_health(self):
        response = self.client.get('/application/health')
        self.assertEqual(response.status_code, 200)
