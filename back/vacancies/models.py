from django.db import models
from companies.models import Company
from utils import UniqueFileName, FileSizeValidator


class SimpleVacancy(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to=UniqueFileName('vacancies/simplevacancies'), blank=True, null=True, validators=[FileSizeValidator(2)])
    created_at = models.DateField(auto_now=True)

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
    image = models.ImageField(upload_to=UniqueFileName('vacancies/images'), blank=True, null=True, validators=[FileSizeValidator(2)])
    attachment = models.FileField(upload_to=UniqueFileName('vacancies/attachments'), blank=True, null=True, validators=[FileSizeValidator(2)])
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
