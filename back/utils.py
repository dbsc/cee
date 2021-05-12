from rest_framework.fields import ModelField
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify
from os.path import splitext, join
from uuid import uuid4


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


@deconstructible
class UniqueFileName(object):

    def __init__(self, path):
        self.path = join(path, "%s%s")

    def __call__(self, instance, filename):
        name = slugify(str(instance)) + str(uuid4())
        extension = splitext(filename)[1]
        return self.path % (name, extension)


@deconstructible
class FileSizeValidator(object):

    def __init__(self, max_size):
        self.max_size = mb_to_bytes(max_size)

    def __call__(self, file):
        if file.size > self.max_size:
            raise ValidationError("File size cannot exceed %.2fMiB" % self.max_size_in_mb)

    @property
    def max_size_in_mb(self):
        return bytes_to_mb(self.max_size)


def mb_to_bytes(size):
    return 1024 * 1024 * size


def bytes_to_mb(size):
    return size / (1024 * 1024)