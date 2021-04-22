from rest_framework import serializers

from companies.serializers import CompanySerializer
from .models import (
    Position, Responsability, SimpleVacancy, Skill,
    Tag, Vacancy, Requirement, Field
)


class SimpleVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleVacancy
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    requirements = serializers.StringRelatedField(many=True)
    company = CompanySerializer()
    field = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

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


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ResponsabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsability
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'