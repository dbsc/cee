from django.db import models
from utils import FileSizeValidator, UniqueFileName
from django.core.validators import FileExtensionValidator


def logo_path(instance, filename):
    basedir = 'companies'
    ext = filename.split('.')[-1]
    return f'{basedir}/{instance.name.lower()}.{ext}'


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.FileField(
        validators=[FileSizeValidator(2), FileExtensionValidator(['svg', 'png'])],
        upload_to=logo_path
    )
    careers = models.URLField(
        max_length=350,
        blank=True,
    )
    featured = models.BooleanField(
        blank=True,
        default=False
    )
    # TODO: culture

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
