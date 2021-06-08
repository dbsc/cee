from django.db import models
from django.db.models.query import QuerySet
from companies.models import Company
from vacancies.models import Field, Tag
from datetime import timedelta
from django.utils import timezone
from django.db.models import F


class EventQuerySet(QuerySet):
    """Custom Event Queryset"""

    def upcoming(self):
        return self.filter(datetime__lt=timezone.now()).order_by('datetime')

    def now(self):
        return self.filter(
            datetime__lte=timezone.now(),
            datetime__gte=timezone.now() - F('duration')
        ).order_by('datetime')

    def past(self):
        return self.filter(
            datetime__lt=timezone.now() - F('duration')
        ).order_by('datetime')

    def today(self):
        return self.filter(
            datetime__today=timezone.now().day,
            datetime__gte=timezone.now() - F('duration')
        ).order_by('datetime')


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
    featured = models.BooleanField(
        default=False,
        blank=False,
        help_text="Whether the event is more important than others."
    )

    objects = EventQuerySet.as_manager()

    def upcoming(self):
        """Whether this is an upcoming event."""
        return timezone.now() < self.datetime

    def will_happen_soon(self, time_interval=timedelta(weeks=1)):
        """Whether this event will happen soon."""
        return self.datetime <= timezone.now() + time_interval

    def already_happened(self):
        """Whether this event already happened."""
        return self.datetime + self.duration < timezone.now()

    def is_happening(self):
        """Whether this event is happening right now."""
        return self.datetime <= timezone.now() <= self.datetime + self.duration

    def will_happen_today(self):
        """Whether this event will happen today."""
        return self.datetime.day == timezone.now().day
