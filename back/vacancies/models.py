from os import name
from django.core.exceptions import ValidationError
from django.db import models
from companies.models import Company


def upload_location(instance, filename):
    name, extension = filename.split('.')
    return 'images/vacancies/%s.%s' % (instance.name, extension)


def file_size_validator(limit):
    def check_file_size(value):
        if value.size > limit:
            raise ValidationError("File size should not exceed 2 MiB")
    return check_file_size(limit)


class SimpleVacancy(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    file = models.FileField(upload_to=upload_location, blank=True, null=True, validators=file_size_validator(2 * 1024 * 1024))

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    field = models.ForeignKey('Field', on_delete=models.PROTECT, blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.PROTECT, blank=True, null=True)
    pay = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    link = models.URLField(max_length=400, blank=True)
    requirements = models.ManyToManyField('Requirement')

    def __str__(self):
        return self.name


class Requirement(models.Model):
    requirement = models.CharField(max_length=300)
    vancancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.requirement


class Field(models.Model):
    name = models.CharField(max_length=150)


class Position(models.Model):
    position = models.CharField(max_length=150)