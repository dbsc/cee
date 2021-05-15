from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
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
from .fields import RequirementNestedField

from companies.serializers import CompanySerializer


class SimpleVacancyViewSet(ModelViewSet):
    """Returns a list of the all the SimpleVacancy objects."""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SimpleVacancy.objects.all()
    serializer_class = SimpleVacancySerializer


class VacancyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @action(detail=True)
    def responsibilities(self, request, pk=None):
        """List all the responsibilities regarding the vacancy"""
        vacancy = self.get_object()
        responsibilities = vacancy.responsibilities.all()
        serializer = ResponsibilitySerializer(responsibilities, many=True, fields=['id', 'description'])
        return Response(serializer.data)

    @action(detail=True)
    def company(self, request, pk=None):
        """Detail of vacancy's company"""
        vacancy = self.get_object()
        company = vacancy.company
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    @action(detail=True, methods=['GET', 'POST'])
    def requirements(self, request, pk=None):
        """List all the vacancy's requirements, or create new requirements"""
        if request.method == 'GET':
            vacancy = self.get_object()
            requirements = vacancy.requirements.all()
            serializer = RequirementSerializer(requirements, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            vacancy = self.get_object()
            serializer = RequirementNestedField(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

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

    @action(detail=True, methods=[])
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
