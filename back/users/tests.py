from django.test import TestCase
from .models import CustomUser


class TestCustomUser(TestCase):

    def test_create_user(self):
        user_data = {
            'nickname': 'Batata',
            'email': "andredalbosco2020@gmail.com",
            'password': 'secret',
        }
        user = CustomUser.objects.create_user(**user_data)
