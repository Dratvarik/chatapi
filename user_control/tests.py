# Create your tests here.
from rest_framework.test import APITestCase
from .views import get_random, get_access_token, get_refresh_token


class TestGenericFunctions(APITestCase):
    def test_get_random(self):
        r1=get_random(10)
        r2=get_random(10)
        r3=get_random(15)

        self.assertTrue(r1)

        self.assertNotEqual(r1, r2)

        self.assertEqual(len(r1), 11)
        self.assertEqual(len(r3), 15)