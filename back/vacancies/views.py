from rest_framework import permissions
from rest_framework import viewsets

from .models import SimpleVacancy, Vacancy, Requirement, Field, Position
from .serializers import (
    SimpleVacancySerializer, VacancySerializer, RequirementSerializer,
    FieldSerializer, PositionSerializer
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