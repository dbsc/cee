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
            email='andre@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_create_company(self):
        data = google.copy()
        url = reverse('companies:company-list')
        data['logo'] = open('data/logo/google.svg')
        # fp = open('data/logo/google.svg', 'r')
        # data['logo'] = fp
        # print(type(data['logo']))

        response = self.client.post(url, data, format='json')
        # response = self.post_company(data)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

        company = Company.objects.get(name=data['name'])
        self.assertEqual(company.name, data['name'])
        self.assertEqual(company.featured, data['featured'])
        self.assertEqual(company.careers, data['careers'])

    # def test_create_company_blank_or_null_name(self):
        # url = reverse('companies:company-list')
    #     data = google.copy()

    #     data['name'] = ""
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Company.objects.count(), 0)

    #     data['name'] = None
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Company.objects.count(), 0)

    # def test_create_company_blank_career(self):
    #     url = reverse('companies:company-list')
    #     data = google.copy()

    #     data['careers'] = ""
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Company.objects.count(), 1)

    #     company = Company.objects.get()
    #     self.assertEqual(company.careers, "")

    # def test_create_company_null_career(self):
    #     url = reverse('companies:company-list')
    #     data = google.copy()

    #     data['careers'] = None
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Company.objects.count(), 1)

    #     company = Company.objects.get()
    #     self.assertEqual(company.careers, "")

    def post_company(self, data={}, use_base=True):
        if use_base:
            data = {**data, **self.base}
        with open(data['logo'], 'r') as logo:
            url = reverse('companies:company-list')
            data['logo'] = logo
            response = self.client.post(url, data, format='json')
        return response
