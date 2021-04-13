# from rest_framework import generics
from rest_framework import viewsets

from .models import SimpleVacancy, Vacancy, Requirement, Field
from .serializers import (
    SimpleVacancySerializer, VacancySerializer, RequirementSerializer, FieldSerializer
)


class SimpleVacancyViewSet(viewsets.ModelViewSet):
    queryset = SimpleVacancy.objects.all()
    serializer_class = SimpleVacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

