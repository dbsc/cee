from django.db import models
from companies.models import Company
from vacancies.models import Field, Tag
from datetime import timedelta


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    datetime = models.DateTimeField()
    duration = models.DurationField(default=timedelta(hours=1))
    image = models.ImageField()
    link = models.URLField()
    field = models.ForeignKey(
        Field,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
