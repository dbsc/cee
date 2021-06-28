import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cee.settings")
import django
django.setup()

import json
from django.core.files import File
from companies.models import Company
from contextlib import contextmanager
from vacancies.serializers import VacancySerializer

def create_companies():
    with open(file_path('companies.json'), 'r') as fp:
        companies = json.load(fp)
        for data in companies:
            with multipart(data, ['logo']) as company:
                if not Company.objects.filter(name=company['name']).exists():
                    Company.objects.create(**company)


def create_vacancies():
    with open(file_path('vacancies.json'), 'r') as fp:
        vacancies = json.load(fp)
        for vacancy_data in vacancies:
            with multipart(vacancy_data, ['image', 'attachment']) as data:
                company = Company.objects.get(name=data['company'])
                data.update(company=company.pk)
                serializer = VacancySerializer(data=data)
                serializer.is_valid()
                serializer.save()


def file_path(filename):
    return os.path.join('data', filename)


@contextmanager
def multipart(data, file_fields=[]):
    resources = {}
    for field in set(file_fields).intersection(data):
        try:
            resources[field] = open(data[field], 'rb')
        except (FileNotFoundError, TypeError):
            pass
    try:
        files = {key: File(b) for key, b in resources.items()}
        yield {**data, **files}
    finally:
        for resource in resources.values():
            resource.close()


if __name__ == '__main__':
    create_companies()
    create_vacancies()
