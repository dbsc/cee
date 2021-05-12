from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    SimpleVacancy, Vacancy, Requirement,
    Position, Tag, Responsibility, Field
)
from .serializers import (
    SimpleVacancySerializer, VacancySerializer, RequirementSerializer,
    FieldSerializer, PositionSerializer, TagSerializer,
    ResponsibilitySerializer
)
from companies.serializers import CompanySerializer


class SimpleVacancyViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SimpleVacancy.objects.all()
    serializer_class = SimpleVacancySerializer


class VacancyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @action(detail=True)
    def responsibilities(self, request, pk=None):
        vacancy = self.get_object()
        responsibilities = vacancy.responsibilities.all()
        serializer = ResponsibilitySerializer(responsibilities, many=True, fields=['id', 'description'])
        return Response(serializer.data)

    @action(detail=True)
    def company(self, request, pk=None):
        vacancy = self.get_object()
        company = vacancy.company
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    @action(detail=True)
    def requirements(self, request, pk=None):
        vacancy = self.get_object()
        requirements = vacancy.requirements.alL()
        serializer = RequirementSerializer(requirements, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def tags(self, request, pk=None):
        vacancy = self.get_object()
        tags = vacancy.tags.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def position(self, request, pk=None):
        vacancy = self.get_object()
        position = vacancy.position
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    @action(detail=True)
    def field(self, request, pk=None):
        vacancy = self.get_object()
        field = vacancy.field
        serializer = FieldSerializer(field)
        return Response(serializer.data)



class RequirementViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class FieldViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class PositionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class TagViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ResponsibilityViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer
