
from unittest import TestCase

from rest_framework.test import APIClient, APITestCase


class TestSomething(APITestCase):
    def test_sample_view(self):
        client = APIClient()
        URL = "/test/"
        response = client.get(URL)
        assert response.status_code == 200