from .models import Event
from rest_framework import serializers
from vacancies.fields import FieldField, TagField


class EventSerializer(serializers.ModelSerializer):
    tags = TagField(many=True)
    field = FieldField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'datetime',
            'duration',
            'image',
            'link',
            'field',
            'company',
            'tags'
        ]

    def create(self, validated_data):
        tag_names = validated_data.pop('tags')
        field_name = validated_data.pop('field')

