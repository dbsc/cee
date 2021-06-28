from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from vacancies.models import Field, Position, Vacancy
from companies.models import Company
from users.models import CustomUser
from utils import multipart


class VacancyTest(TestCase):

    def test_vacancy(self):
        pass


class VacancyAPITest(APITestCase):
    companies = [
        {
            "name": "Google",
            "logo": "data/logo/google.svg",
            "careers": "https://careers.google.com/jobs/",
        },
        {
            "name": "Apple",
            "logo": "data/logo/apple.svg",
            "careers": "https://www.apple.com/careers/br/",
        },
    ]

    base = {
        'title': "This is a title",
        'company': 'Google',
        'description': 'This is a description.',
        'requirements': {
            'minimum': ['minimum requirement'],
            'preferred': ['preferred requirement'],
            'none': ['none requirement'],
        },
        'responsibilities': [
            'responsibility one',
            'responsibility two',
        ],
        'field': 'Some field',
        'position': 'Some position',
        'tags': [
            'Tag one',
            'Tag two',
        ],
        'pay': 12500,
        'link': 'http://example.com',
        'expiration_date': None,
        'image': 'data/img/vtex.jpg',
        'attachment': 'data/pdf/vacancy.pdf',
        'remote': False,
        'location': {
            'city': 'São Paulo',
            'state': 'SP',
        },
        'featured': False,
    }

    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email='user@example.com',
            password='secret'
        )
        self.client.force_login(self.user)
        for data in self.companies:
            self.post_company(**data)

    def test_vacancy_create(self):
        data = self.base.copy()
        response = self.post_vacancy(**data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vacancy_blank_title(self):
        response = self.post_vacancy(title='')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_missing_title(self):
        response = self.post_vacancy(missing=['title'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_blank_company(self):
        response = self.post_vacancy(company=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_missing_company(self):
        response = self.post_vacancy(missing=['company'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_blank_description(self):
        response = self.post_vacancy(description='')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_missing_description(self):
        response = self.post_vacancy(missing=['company'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_vacancy_blank_requirements(self):
    #     requirements = None
    #     response = self.post_vacancy(requirements=requirements)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #     requirements = {}
    #     response = self.post_vacancy(requirements=requirements)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     requirements = {'minimum': ['ab'], 'preferred': []}
    #     response = self.post_vacancy(requirements=requirements)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vacancy_missing_requirements(self):
        response = self.post_vacancy(missing=['requirements'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_responsibilities(self):
    #     responsibilities = []
    #     response = self.post_vacancy(responsibilities=responsibilities)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     responsibilities = ['']
    #     response = self.post_vacancy(responsibilities=responsibilities)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #     responsibilities = None
    #     response = self.post_vacancy(responsibilities=responsibilities)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vacancy_missing_responsibilities(self):
        response = self.post_vacancy(missing=['responsibilities'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_field(self):
    #     # TODO
    #     response = self.post_vacancy(field=None)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     response = self.post_vacancy(field='')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vacancy_missing_field(self):
        response = self.post_vacancy(missing=['field'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_position(self):
    #     response = self.post_vacancy(position='')
    #     print(response.content)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vacancy_missing_position(self):
        response = self.post_vacancy(missing=['position'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_vacancy_blank_tags(self):
    #     pass

    def test_vacancy_missing_tags(self):
        response = self.post_vacancy(missing=['tags'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_pay(self):
    #     pass

    def test_vacancy_missing_pay(self):
        response = self.post_vacancy(missing=['pay'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacancy = Vacancy.objects.get()
        self.assertIsNone(vacancy.pay)

    # def test_vacancy_blank_link(self):
    #     pass

    def test_vacancy_missing_link(self):
        response = self.post_vacancy(missing=['link'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacancy = Vacancy.objects.get()
        self.assertEqual(vacancy.link, '')

    # def test_vacancy_blank_expiration_date(self):
    #     pass

    def test_vacancy_missing_expiration_date(self):
        response = self.post_vacancy(missing=['expiration_date'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacancy = Vacancy.objects.get()
        self.assertIsNone(vacancy.expiration_date)

    # def test_vacancy_blank_image(self):
    #     pass

    def test_vacancy_missing_image(self):
        response = self.post_vacancy(missing=['image'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_attachment(self):
    #     pass

    def test_vacancy_missing_attachment(self):
        response = self.post_vacancy(missing=['attachment'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_remote(self):
    #     pass

    def test_vacancy_missing_remote(self):
        response = self.post_vacancy(missing=['remote'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacancy = Vacancy.objects.get()
        self.assertFalse(vacancy.remote)

    # def test_vacancy_blank_location(self):
    #     pass

    def test_vacancy_missing_location(self):
        response = self.post_vacancy(missing=['location'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_vacancy_blank_featured(self):
    #     pass

    def test_vacancy_missing_featured(self):
        response = self.post_vacancy(missing=['featured'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacancy = Vacancy.objects.get()
        self.assertFalse(vacancy.featured)

    def post_vacancy(self, use_base=True, format='json',
                     missing=[], **kwargs):
        if use_base:
            data = {**self.base, **kwargs}
        else:
            data = kwargs
        for key in missing:
            data.pop(key)
        for key in ('image', 'attachment'):
            if key in data:
                data.pop(key)
        try:
            if isinstance(data['company'], str):
                company = Company.objects.get(name=data['company'])
                data['company'] = company.pk
        except KeyError:
            pass

        url = reverse('vacancies:vacancy-list')
        response = self.client.post(url, data=data, format='json')

        return response

    def post_company(self, format='multipart', **kwargs):
        with multipart(kwargs, ['logo']) as data:
            url = reverse('companies:company-list')
            response = self.client.post(url, data, format=format)

        return response
