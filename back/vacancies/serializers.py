from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from .models import (
    Location, Position, Responsibility, SimpleVacancy,
    Tag, Vacancy, Requirement, Field
)
from .fields import (
    FieldField, RequirementNestedField, ResponsibilityListField,
    TagField, PositionField, LocationField
)
from utils import DynamicFieldsModelSerializer


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'description', 'vacancy', 'minimum', 'preferred']

    def validate(self, data):
        """Check that preferred and minimum are not both True"""
        if data['minimum'] and data['preferred']:
            raise serializers.ValidationError(
                'minimum and preferred cannot both be true')
        return data


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'name']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class ResponsibilitySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Responsibility
        fields = ['id', 'description', 'vacancy']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LocationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'state']

    def validate_city(self, value):
        words = [word.capitalize() for word in value.split()]
        return ' '.join(words)

    def validate_state(self, value):
        return value.upper()


class VacancySerializer(serializers.ModelSerializer):
    tags = TagField(
        many=True,
        help_text='Optional tags for the vacancy.'
    )
    position = PositionField(
        allow_null=True,
        help_text="The vacancy's position."
    )
    responsibilities = ResponsibilityListField(
        help_text="The vacancy's listed responsibilities."
    )
    requirements = RequirementNestedField(
        help_text="The list of requirements. Each requirement can be minimum, preferred or none."
    )
    field = FieldField(
        allow_null=True,
        help_text="The vacancy's working field."
    )
    # location = LocationField(
    #     allow_null=True,
    #     help_text='The location of the job.'
    # )
    location = LocationSerializer(
        fields=['city', 'state'],
        allow_null=True,
        help_text='The location of the job.',
        required=False
    )

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'company',
            'description',
            'requirements',
            'responsibilities',
            'field',
            'position',
            'tags',
            'pay',
            'link',
            'expiration_date',
            'image',
            'attachment',
            'remote',
            'location',
            'featured',
        ]

    def create(self, validated_data):
        field_data = validated_data.pop('field', None)
        position_data = validated_data.pop('position', None)
        location_data = validated_data.pop('location', None)
        responsibilities_data = validated_data.pop('responsibilities', [])
        requirements_data = validated_data.pop('requirements', [])
        tags_data = validated_data.pop('tags', [])
        vacancy = super().create(validated_data)
        if field_data:
            field, created = Field.objects.get_or_create(**field_data)
            field.vacancy_set.add(vacancy)
        if position_data:
            position, created = Position.objects.get_or_create(**position_data)
            position.vacancy_set.add(vacancy)
        if location_data:
            location, created = Location.objects.get_or_create(**location_data)
            location.vacancy_set.add(vacancy)
        for responsibility_data in responsibilities_data:
            vacancy.responsibilities.create(**responsibility_data)
        for requirement_data in requirements_data:
            vacancy.requirements.create(**requirement_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            if not vacancy.tags.filter(pk=tag.pk).exists():
                vacancy.tags.add(tag)
        return vacancy

    def update(self, instance, validated_data):
        for responsibility_data in validated_data.pop('responsibilities', []):
            instance.responsibilities.get_or_create(**responsibility_data)
        for requirement_data in validated_data.pop('requirements', []):
            instance.requirements.get_or_create(**requirement_data)
        for tag_data in validated_data.pop('tags', []):
            tag, created = Tag.objects.get_or_create(**tag_data)
            if not instance.tags.filter(pk=tag.pk).exists():
                instance.tags.add(tag)
        if 'field' in validated_data:
            field_data = validated_data.pop('field')
            field, created = Field.objects.get_or_create(**field_data)
            instance.field = field
        if 'position' in validated_data:
            position_data = validated_data.pop('position')
            position, created = Position.objects.get_or_create(**position_data)
            instance.position = position
        if 'location' in validated_data:
            location_data = validated_data.pop('location')
            location, created = Location.objects.get_or_create(**location_data)
            instance.location = location
        return super().update(instance, validated_data)

    def validate_requirements(self, value):
        try:
            requirements = self.instance.requirements
        except AttributeError:
            pass
        else:
            for requirement in value:
                description = requirement['description']
                if requirements.filter(description=description).exists():
                    raise ValidationError('Cannot have duplicated requirement.')
        return value

    def validate_responsibilities(self, value):
        try:
            responsibilities = self.instance.responsibilities
        except AttributeError:
            pass
        else:
            for description in value:
                if responsibilities.filter(description=description).exists():
                    raise ValidationError('Cannot have duplicated responsibility.')
        return value

    def validate(self, attrs):
        if attrs.get('location') and attrs.get('remote'):
            raise ValidationError('A job cannot have both a location and be remote')


class SimpleVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleVacancy
        fields = [
            'id',
            'title',
            'company',
            'description',
            'expiration_date',
            'attachment',
            'created_at',
        ]
