from collections import OrderedDict
from typing import get_args
from django.db.models.fields import CharField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.fields import ListField
from rest_framework.relations import StringRelatedField
from .models import Field, Position, Requirement, Responsibility, Tag, Vacancy

# 3 possibilidades: relatedfield, listfield ou serializer.


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


class TagRelatedField(serializers.RelatedField):
    default_error_messages = {
        'incorrect_type': _('Incorrect type. Expected string, got {data_type}'),
        'blank': _('This field may not be blank')
    }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise self.fail('incorrect_type', data_type=type(data).__name__)
        if data == '':
            self.fail('blank')
        return {"name": data}

    def to_representation(self, value):
        return str(value)

    def get_queryset(self):
        return Tag.objects.all()


class FieldRelatedField(serializers.RelatedField):
    default_error_messages = {
        'incorrect_type': _('Incorrect type. Expected string, got {data_type}'),
        'blank': _('This field may not be blank')
    }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise self.fail('incorrect_type', data_type=type(data).__name__)
        if data == '':
            self.fail('blank')
        return {"name": data}

    def to_representation(self, value):
        return str(value)


class ResponsibilityRelatedField(serializers.RelatedField):
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


class ResponsibilityListField(serializers.ListField):

    def __init__(self, *args, **kwargs):
        max_length = Responsibility._meta.get_field('description').max_length
        kwargs['child'] = serializers.CharField(max_length=max_length)
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        queryset = data.all()
        return super().to_representation(queryset)


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


class RequirementListField(serializers.ListField):

    def __init__(self, *args, **kwargs):
        max_length = Requirement._meta.get_field('description').max_length
        kwargs['child'] = serializers.CharField(max_length=max_length)
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        queryset = data.all()
        return super().to_representation(queryset)


class RequirementNestedField(serializers.Serializer):

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

    def to_representation(self, instance):
        ret = OrderedDict()
        for name, field in self.get_fields().items():
            representation = field.to_representation(getattr(instance, name)())
            if representation:
                ret[name] = representation
        return ret


class RequirementRelatedField(serializers.RelatedField):
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


class RequirementsField(serializers.Field):
    default_error_messages = {
        'incorrect_type': _('Incorrect type. Expected string, got {data_type}'),
        'blank': _('This field may not be blank')
    }

    def to_internal_value(self, data):
        def requirement_data(description, minimum=False, preferred=False):
            return {
                "description": description,
                "minimum": minimum,
                "preferred": preferred
            }
        minimum = data.get('minimum', [])
        preferred = data.get('preferred', [])
        none = data.get('none', [])
        requirements = []
        for description in minimum:
            requirement = requirement_data(description, minimum=True)
            requirements.append(requirement)
        for description in preferred:
            requirement = requirement_data(description, preferred=True)
            requirements.append(requirement)
        for description in none:
            requirement = requirement_data(description)
            requirements.append(requirement)
        return requirements

    def to_representation(self, value):
        minimum = value.filter(minimum=True)
        preferred = value.filter(preferred=True)
        none = value.filter(minimum=False, preferred=False)
        ret = OrderedDict()
        if minimum:
            ret['minimum'] = [str(obj) for obj in minimum]
        if preferred:
            ret['preferred'] = [str(obj) for obj in preferred]
        if none:
            ret['none'] = [str(obj) for obj in none]
        return ret
