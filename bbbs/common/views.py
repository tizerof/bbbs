from rest_framework import generics

from bbbs.common.models import City, Profile
from bbbs.common.serializers import CitySerializer, ProfileSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
