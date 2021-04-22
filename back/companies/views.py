from rest_framework import permissions
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
