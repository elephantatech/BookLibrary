from fastapi.testclient import TestClient
from main.app import app
from unittest import TestCase


class test_app(TestCase):
    def test_app_home_ok(self):
        client = TestClient(app)
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "This is the home page"})
