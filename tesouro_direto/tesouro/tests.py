from rest_framework import status
from rest_framework.test import APITestCase


class TestApi(APITestCase):
    def test_api_response_success(self):
        response = self.client.get('/titulos/', {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_response_error(self):
        response = self.client.get('/error/', {})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


