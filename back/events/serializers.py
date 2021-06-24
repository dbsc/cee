from .models import Event
from rest_framework import serializers
from vacancies.fields import FieldField, TagField
from vacancies.models import Field, Tag


class EventSerializer(serializers.ModelSerializer):
    tags = TagField(many=True)
    field = FieldField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'datetime',
            'duration',
            'location',
            'company',
            'field',
            'image',
            'link',
            'tags',
            'featured',
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        field_data = validated_data.pop('field')
        event = super().create(validated_data)
        field, created = Field.objects.get_or_create(**field_data)
        field.event_set.add(event)
        for tag_data in tags_data:
            event.tags.create(**tag_data)
        return event

    def update(self, instance, validated_data):
        # TODO: update function
        return super().update(instance, validated_data)
