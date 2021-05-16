from django.db import models
from companies.models import Company
from vacancies.models import Field, Tag
from datetime import timedelta
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(
        max_length=250,
        help_text='The title of the event.'
    )
    description = models.TextField(
        blank=True,
        help_text='The description of the event.'
    )
    datetime = models.DateTimeField(
        blank=True,
        null=True,
        help_text="The date and time of the event."
    )
    duration = models.DurationField(
        default=timedelta(hours=1),
        help_text="The event's duration."
    )
    image = models.ImageField(
        blank=True,
        null=True,
        help_text='An image of the event.'
    )
    link = models.URLField(
        blank=True,
        help_text="The event meeting URL."
    )
    field = models.ForeignKey(
        Field,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="The field of work related to the event."
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="The company related to the event, if there is one."
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        help_text="Optional tags for the event."
    )
    location = models.CharField(
        max_length=250,
        blank=True,
        help_text='The location of the event.'
    )

    def will_happen_soon(self, time_interval=timedelta(weeks=1)):
        return self.datetime <= timezone.now() + time_interval
