from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vacancies.models import Vacancy
from companies.models import Company


class CompanyTest(APITestCase):
    def create_company_test(self):
        url = reverse('companies:company-list')




class VacancyCreateTest(APITestCase):
    pass
