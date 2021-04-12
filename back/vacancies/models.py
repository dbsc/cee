from django.db import models
from companies.models import Company


def upload_location(instance, filename):
    name, extension = filename.split('.')
    return 'images/vacancies/%s.%s' % (instance.name, extension)


class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    field = models.ForeignKey('Field', on_delete=models.PROTECT, blank=True, null=True)
    position = models.CharField(max_length=100)
    # position = models.ForeignKey('Position', on_delete=models.PROTECT, blank=True, null=True)
    pay = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True) # put False later
    expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    link = models.URLField(max_length=400, blank=True)
    # requirements = models.ManyToManyField('Requirement')
    # TODO: position, requirements

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