from django.db import models
from utils import FileSizeValidator, UniqueFileName


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(
        upload_to=UniqueFileName('companies/logos'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True
    )
    careers = models.URLField(
        max_length=350,
        blank=True,
        null=True
    )
    # TODO: culture

    def __str__(self):
        return self.name
