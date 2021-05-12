from django.db import models
from django.db.models.fields import BooleanField
from django.core.exceptions import ValidationError
from companies.models import Company
from utils import UniqueFileName, FileSizeValidator
from datetime import date
models.CharField

class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    field = models.ForeignKey(
        'Field',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        'Position',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True
    )
    pay = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=UniqueFileName('vacancies/images'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True
    )
    attachment = models.FileField(
        upload_to=UniqueFileName('vacancies/attachments'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True
    )
    link = models.URLField(
        max_length=400,
        blank=True
    )
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        """Returns True if the vacancy is still active"""
        return date.today() <= self.expiration_date and self.active


class RequirementQuerySet(models.QuerySet):

    def minimum(self):
        return self.filter(minimum=True)

    def preferred(self):
        return self.filter(preferred=True)

    def none(self):
        return self.filter(minimum=False, preferred=False)


class Requirement(models.Model):
    description = models.CharField(max_length=300)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='requirements'
    )
    minimum = BooleanField(default=False)
    preferred = BooleanField(default=False)
    objects = RequirementQuerySet.as_manager()

    class Meta:
        ordering = ['vacancy', 'minimum', 'preferred']

    def __str__(self):
        return self.description

    @property
    def none(self):
        return not self.minimum and not self.preferred

    def clean(self):
        super().clean()
        if self.minimum and self.preferred:
            raise ValidationError(
                "Requirement's minimum and preferred fields cannot both be true."
            )

    def save(self, *args, **kwargs):
        if self.minimum and self.preferred:
            return
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Responsibility(models.Model):
    description = models.CharField(max_length=200)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='responsibilities'
    )

    class Meta:
        verbose_name_plural = 'responsibilities'

    def __str__(self):
        return self.description


class Field(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SimpleVacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=150)
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    attachment = models.FileField(
        upload_to=UniqueFileName('vacancies/simplevacancies'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "simple vacancies"

    def __str__(self):
        return self.name
