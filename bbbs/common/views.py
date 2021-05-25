from rest_framework import generics, viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from bbbs.common.models import City, Profile
from bbbs.common.role_types import RoleTypes
from bbbs.common.serializers import CitySerializer, ProfileSerializer
from bbbs.utils.utils import has_roles


class CityViewSet(viewsets.ViewSet):

    @has_roles([RoleTypes.REGIONAL_MODERATOR.value, RoleTypes.MENTOR.value])
    @staticmethod
    def list(request: Request) -> Response:
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response({'cities': serializer.data})

    def change_user_city(self, request: Request, user_id: int) -> Response:
        profile_id = Profile.objects.get(user__id=user_id).id
        serializator = ProfileSerializer(profile_id, data=request.data, partial=True)
        serializator.is_valid(raise_exception=True)
        serializator.save()
        return Response({'success': 'ok'}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=self.request.user)
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
