from django.db import models


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pay = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    expiration_date = models.DateField()
