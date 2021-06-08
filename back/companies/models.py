from django.db import models
from utils import FileSizeValidator, UniqueFileName


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(
        upload_to=UniqueFileName('companies/logos'),
        validators=[FileSizeValidator(2)],
        null=True
    )
    careers = models.URLField(
        max_length=350,
        blank=True,
    )
    featured = models.BooleanField(
        blank=True,
        null=True,
        default=False
    )
    # TODO: culture

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
