
from unittest import TestCase

from rest_framework.api import APIClient


class TestSomething(APIClient):
    def test_sample_view()
        client = APIClient()
        URL = "/test/"
        response = client.get(URL)
        assert response.status_code == 200