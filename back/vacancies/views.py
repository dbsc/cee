# from rest_framework import generics
from rest_framework import viewsets

from .models import Vacancy, Requirement, Field
from .serializers import (
    VacancySerializer, RequirementSerializer, FieldSerializer
)


# class VacancyList(generics.ListCreateAPIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancySerializer



# class VacancyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
