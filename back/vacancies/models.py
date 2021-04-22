from django.db import models
from companies.models import Company
from utils import UniqueFileName, FileSizeValidator
from datetime import date


class SimpleVacancy(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to=UniqueFileName('vacancies/simplevacancies'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True
    )
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=150)
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
    pay = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)
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
    tags = models.ManyToManyField(
        'Tag',
        blank=True
    )

    # class Meta:
    #     ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return date.today() <= self.expiration_date

    # @property
    # def requirements(self):
    #     return self.requirement_set.all()


class Requirement(models.Model):
    name = models.CharField(max_length=300)
    vancancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='requirements'
    )
    # TODO: preferred/minimum

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Responsability(models.Model):
    name = models.CharField(max_length=200)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

