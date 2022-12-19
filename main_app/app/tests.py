from django.urls import reverse
from rest_framework.test import APITestCase


class OdderTests(APITestCase):
    def test_odd_correct(self):
        url = reverse('odder', args=[1, 2])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 1,
            "second": 2,
            "result": [1]
        })
