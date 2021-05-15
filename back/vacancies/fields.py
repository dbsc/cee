from collections import OrderedDict
from typing import get_args
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from .models import Field, Position, Requirement, Responsibility, Tag, Vacancy

class FieldField(serializers.CharField, serializers.RelatedField):

    def __init__(self, **kwargs):
        kwargs.update(
            max_length=Field.name.field.max_length,
            # allow_blank = Field.name.field.blank
            allow_blank=Vacancy.field.field.blank  # TODO: remove this
        )
        many = kwargs.pop('many', False)
        serializers.RelatedField.__init__(self, many=many)
        super().__init__(**kwargs)

    def get_queryset(self):
        return Field.objects.all()

    def run_validation(self, data):
        if data == '' or (self.trim_whitespace and str(data).strip() == ''):
            if not self.allow_blank:
                self.fail('blank')
        return serializers.Field.run_validation(self, data)

    def to_internal_value(self, data):
        name = super().to_internal_value(data)
        return {"name": name}


class TagField(serializers.CharField, serializers.RelatedField):

    def __init__(self, **kwargs):
        kwargs.update(
            max_length=Tag.name.field.max_length,
            allow_blank=Tag.name.field.blank
        )
        serializers.RelatedField.__init__(self)
        super().__init__(**kwargs)

    def get_queryset(self):
        return Tag.objects.all()

    def to_internal_value(self, data):
        name = super().to_internal_value(data)
        return {"name": name}


class TagListField(serializers.ListField):

    def __init__(self, *args, **kwargs):
        kwargs['child'] = serializers.CharField(
            allow_blank=Tag.name.field.blank,
            max_length=Tag.name.field.max_length
        )
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        queryset = data.all()
        return super().to_representation(queryset)


class PositionField(serializers.CharField, serializers.RelatedField):

    def __init__(self, **kwargs):
        kwargs.update(
            max_length=Position.name.field.max_length,
            allow_blank=True
            # allow_blank=Position.name.field.blank
        )
        serializers.RelatedField.__init__(self)
        super().__init__(**kwargs)

    def get_queryset(self):
        return Position.objects.all()

    def run_validation(self, data):
        if data == '' or (self.trim_whitespace and str(data).strip() == ''):
            if not self.allow_blank:
                self.fail('blank')
        return serializers.Field.run_validation(self, data)

    def to_internal_value(self, data):
        name = super().to_internal_value(data)
        return {"name": name}


class ResponsibilityListField(serializers.ListField):

    def __init__(self, *args, **kwargs):
        max_length = Responsibility._meta.get_field('description').max_length
        kwargs['child'] = serializers.CharField(max_length=max_length)
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        queryset = data.all()
        return super().to_representation(queryset)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return [{"description": description} for description in data]


class PositionRelatedField(serializers.RelatedField):
    default_error_messages = {
        'incorrect_type': _('Incorrect type. Expected string, got {data_type}'),
        'blank': _('This field may not be blank')
    }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise self.fail('incorrect_type', data_type=type(data).__name__)
        if data == '':
            self.fail('blank')
        return {"description": data}

    def to_representation(self, value):
        return str(value)

    def get_queryset(self):
        return Responsibility.objects.all()


class RequirementNestedField(serializers.Serializer):

    class InnerList(serializers.ListField):

        def __init__(self, cls, field_name, *args, **kwargs):
            max_length = cls._meta.get_field(field_name).max_length
            kwargs['child'] = serializers.CharField(max_length=max_length)
            super().__init__(*args, **kwargs)
            self.target_field = field_name

        def to_representation(self, data):
            return super().to_representation(data)

    class MinimumListField(serializers.ListField):

        def __init__(self, *args, **kwargs):
            max_length = Requirement._meta.get_field('description').max_length
            kwargs['child'] = serializers.CharField(max_length=max_length)
            super().__init__(*args, **kwargs)

    class PreferredListField(serializers.ListField):

        def __init__(self, *args, **kwargs):
            max_length = Requirement._meta.get_field('description').max_length
            kwargs['child'] = serializers.CharField(max_length=max_length)
            super().__init__(*args, **kwargs)

    class NoneListField(serializers.ListField):

        def __init__(self, *args, **kwargs):
            max_length = Requirement._meta.get_field('description').max_length
            kwargs['child'] = serializers.CharField(max_length=max_length)
            super().__init__(*args, **kwargs)

    minimum = MinimumListField(required=False)
    preferred = PreferredListField(required=False)
    none = NoneListField(required=False)

    class Meta:
        fields = ['minimum', 'preferred', 'none']
        # extra_kwargs = {
        #     'minimum': {'required': False},
        #     'preferred': {'required': False},
        #     'none': {'required': False},
        # }
        # validators = []

    # def to_representation(self, instance):
    #     ret = OrderedDict()
    #     for name, field in self.get_fields().items():
    #         queryset = getattr(instance, name)()
    #         representation = field.to_representation(queryset)
    #         if representation:
    #             ret[name] = representation
    #     return ret

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_internal_value(self, data):
        def requirement_data(description, minimum=False, preferred=False):
            return {
                "description": description,
                "minimum": minimum,
                "preferred": preferred
            }
        data = super().to_internal_value(data)
        minimum = data.get('minimum', [])
        preferred = data.get('preferred', [])
        none = data.get('none', [])
        requirements = []
        for description in minimum:
            requirements.append(requirement_data(description, minimum=True))
        for description in preferred:
            requirements.append(requirement_data(description, preferred=True))
        for description in none:
            requirements.append(requirement_data(description))
        return requirements
