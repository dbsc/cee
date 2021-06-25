from datetime import timedelta, timezone
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST


from .models import Email
from .serializers import EmailSerializer


class EmailViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    @action(methods=['POST'], detail=True)
    def send(self, request, pk=None):
        """Send email."""
        serializer = EmailSerializer(data=request.data)
        email = self.get_object()

        if serializer.is_valid():
            email.send(serializer.validated_data)
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            status=HTTP_400_BAD_REQUEST
        )
