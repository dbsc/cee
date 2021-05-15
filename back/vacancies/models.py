from django.db import models
from django.db.models.fields import BooleanField
from django.core.exceptions import ValidationError
from django.utils import timezone
from companies.models import Company
from utils import UniqueFileName, FileSizeValidator
from datetime import date, timedelta


class Vacancy(models.Model):
    """
    Stores a single vacancy, related to :model:`companies.Company`,
    :model:`vacancies.Field`, :model:`vacancies.Position`,
    :model:`vacancies.Tag`, :model:`vancacies.Responsibility` and
    :model:`vacancies.Requirement`.
    """
    title = models.CharField(
        max_length=150,
        help_text="A short title for the vacancy."
    )
    description = models.TextField(
        blank=True,
        help_text="The vacancy's description."
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="The company that provides the job vacancy."
    )
    field = models.ForeignKey(
        'Field',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="The field of work."
    )
    position = models.ForeignKey(
        'Position',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="The vacancy's position."
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        help_text="Optional tags for the vacancy."
    )
    pay = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Amount of pay for the job."
    )
    expiration_date = models.DateField(
        blank=True,
        null=True,
        help_text="The expiration date, if there is one."
    )
    image = models.ImageField(
        upload_to=UniqueFileName('vacancies/images'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True,
        help_text="Optional image field for the vacancy."
    )
    attachment = models.FileField(
        upload_to=UniqueFileName('vacancies/attachments'),
        validators=[FileSizeValidator(2)],
        blank=True,
        null=True,
        help_text="Optional attachment field for the vacancy."
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        help_text="The vacancy's url."
    )
    active = models.BooleanField(
        default=True,
        help_text="Instead of deleting the vacancy, just set this field to false."
    )
    # TODO: location or remote
    # TODO: email para mandar

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        """True if the vacancy is still active, False otherwise."""
        return date.today() <= self.expiration_date and self.active

    def almost_expired(self, time_interval=timedelta(weeks=1)):
        if self.expiration_date:
            return self.expiration_date <= timezone.now() + time_interval
        return False


class RequirementQuerySet(models.QuerySet):
    """Custom QuerySet to filter requirements according to type."""

    def minimum(self):
        """Retrieve the minimum requirements."""
        return self.filter(minimum=True)

    def preferred(self):
        """Retrieve the preferred requirements."""
        return self.filter(preferred=True)

    def none(self):
        """Retrieve requirements which are not minimum nor preferred."""
        return self.filter(minimum=False, preferred=False)


class Requirement(models.Model):
    """Represents a requirement of a given :model:`Vacancy`."""
    description = models.CharField(
        max_length=300,
        help_text="The requirement's description."
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='requirements',
        help_text='The related vacancy.'
    )
    minimum = BooleanField(
        default=False,
        help_text='Denotes whether this is a minimum requirement.'
    )
    preferred = BooleanField(
        default=False,
        help_text='Denotes whether this is a preferred requirement.'
    )
    objects = RequirementQuerySet.as_manager()

    class Meta:
        ordering = ['vacancy', 'minimum', 'preferred']

    def __str__(self):
        return self.description

    @property
    def none(self):
        """Returns False if requirement is minimum or preferred, True otherwise"""
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
    """Stores a single tag, related to :model:`vacancies.Vacancy`."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Responsibility(models.Model):
    """Responsibility model"""
    description = models.CharField(
        max_length=200,
        help_text="The responsibility's description."
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='responsibilities',
        help_text='The related vacancy.'
    )

    class Meta:
        verbose_name_plural = 'responsibilities'

    def __str__(self):
        return self.description


class Field(models.Model):
    """Stores a single field."""
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
