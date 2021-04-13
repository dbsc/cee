from django.db import models
from string import whitespace


def upload_location(instance, filename):
    _, extension = filename.split('.')
    name, _ = instance.name.replace(whitespace, '_')
    return 'companies/%s.%s' % (name, extension)


class Company(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
