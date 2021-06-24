from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from vacancies.models import Vacancy
from companies.models import Company
from users.models import CustomUser

google = {
    'name': "Google",
    'careers': "https://careers.google.com",
    'featured': True,
    'logo': 'data/logo/google.svg'
}

class CompanyTest(APITestCase):
    base = google

    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email='user@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_create_company(self):
        data = google.copy()

        response = self.post_company(**data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

        company = Company.objects.get(name=data['name'])
        self.assertEqual(company.name, data['name'])
        self.assertEqual(company.featured, data['featured'])
        self.assertEqual(company.careers, data['careers'])

    def test_create_company_blank_name(self):
        response = self.post_company(name='')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)

    def test_create_company_missing_name(self):
        response = self.post_company(missing=['name'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)

    def test_create_company_blank_career(self):
        response = self.post_company(careers='')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_create_company_missing_career(self):
        response = self.post_company(missing=['careers'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_create_company_blank_logo(self):
        response = self.post_company(missing=['name'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)

    def test_create_company_featured(self):
        response = self.post_company(featured=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=1)
        self.assertEqual(company.featured, True)

        response = self.post_company(featured=False)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=2)
        self.assertEqual(company.featured, False)

    def test_create_company_alternate_featured(self):
        response = self.post_company(featured='null')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.post_company(featured='false')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=1)
        self.assertEqual(company.featured, False)

        response = self.post_company(featured='true')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=2)
        self.assertEqual(company.featured, True)

    def test_create_company_missing_featured(self):
        response = self.post_company(missing=['featured'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

        company = Company.objects.get()
        self.assertEqual(company.featured, False)

    def post_company(self, use_base=True, format='multipart',
                     missing=[], **kwargs):
        if use_base:
            data = {**self.base, **kwargs}
        else:
            data = kwargs
        for key in missing:
            data.pop(key)
        url = reverse('companies:company-list')
        if 'logo' in data:
            with open(data['logo'], 'rb') as logo:
                data['logo'] = logo
                response = self.client.post(url, data, format=format)
        else:
            response = self.client.post(url, data, format=format)

        return response
