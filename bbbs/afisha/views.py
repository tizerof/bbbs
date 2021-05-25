from rest_framework import generics, viewsets

from rest_framework.request import Request
from rest_framework.response import Response

from bbbs.afisha.models import Event, EventParticipant
from bbbs.afisha.serializers import EventSerializer, EventParticipantSerializer
from bbbs.common.models import Profile


class EventViewSet(viewsets.ViewSet):

    def get_events_by_user(self, request: Request, city_id: int = None):
        if request.user.id:
            user_profile = Profile.objects.get(user__id=request.user.id)
            user_city_id = user_profile.city.id
            events_queryset = Event.objects.filter(city__id=user_city_id)
            serializer = EventSerializer(events_queryset, many=True)
            return Response({'events': serializer.data})
        events_queryset = Event.objects.filter(city__id=city_id)
        serializer = EventSerializer(events_queryset, many=True)
        return Response({'events': serializer.data})


class EventParticipantList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
