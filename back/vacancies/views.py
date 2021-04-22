from rest_framework import permissions
from rest_framework import viewsets

from .models import (
    SimpleVacancy, Skill, Vacancy, Requirement,
    Field, Position, Tag, Responsability
)
from .serializers import (
    SimpleVacancySerializer, VacancySerializer, RequirementSerializer,
    FieldSerializer, PositionSerializer, SkillSerializer, TagSerializer,
    ResponsabilitySerializer
)


class SimpleVacancyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SimpleVacancy.objects.all()
    serializer_class = SimpleVacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class RequirementViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class FieldViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class PositionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ResponsabilityViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Responsability.objects.all()
    serializer_class = ResponsabilitySerializer
