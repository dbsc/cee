from datetime import timedelta, timezone
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from events.models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['GET'], detail=False)
    def upcoming(self, request):
        events = Event.objects.upcoming().order_by('datetime')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def soon(self):
        events = Event.objects.upcoming().filter(
            datetime__lt=timezone.now() + timedelta(weeks=1)
        )
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def past(self):
        events = Event.objects.past()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def now(self):
        events = Event.objects.now()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def today(self):
        events = Event.objects.today()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def featured(self):
        events = Event.objects.filter(featured=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
