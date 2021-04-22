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

    def __str__(self):
        return self.name
