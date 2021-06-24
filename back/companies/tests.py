from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from vacancies.models import Vacancy
from companies.models import Company
from users.models import CustomUser


class CompanyTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email='andre@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_create_company(self):
        url = reverse('companies:company-list')
        data = {
            'name': "ABC Company",
            'careers': "https://example.com",
            'featured': True,
            'logo': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        company = Company.objects.get(name="ABC Company")
        self.assertEqual(company.name, data['name'])
        self.assertEqual(company.featured, data['featured'])
        self.assertEqual(company.careers, data['careers'])

    def test_create_company_blank_name(self):
        url = reverse('companies:company-list')
        data = {
            'name': "",
            'careers': "https://example.com",
            'featured': True,
            'logo': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)

    def test_create_company_blank_career(self):
        url = reverse('companies:company-list')
        data = {
            'name': "ABC Company",
            'careers': "",
            'featured': True,
            'logo': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        company = Company.objects.get()
        self.assertEqual(company.careers, "")

    def test_create_company_null_career(self):
        url = reverse('companies:company-list')
        data = {
            'name': "ABC Company",
            'careers': None,
            'featured': True,
            'logo': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)
