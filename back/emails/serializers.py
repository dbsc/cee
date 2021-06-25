from .models import Email
from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = [
            'id',
            'subject',
            'message',
            'sender',
            'receivers',
            'company',
            'description',
        ]

    def create(self, validated_data):
        email = super().create(validated_data)
        return email