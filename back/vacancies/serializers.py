from rest_framework import serializers
from .models import SimpleVacancy, Vacancy, Requirement, Field


class SimpleVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleVacancy
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
