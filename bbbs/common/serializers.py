from rest_framework import serializers

from bbbs.common.models import City, Profile


class CitySerializer(serializers.Serializer):
    name = serializers.CharField()
    is_primary = serializers.BooleanField()


class ProfileSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    city = serializers.IntegerField()
    roles = serializers.ListField(child=serializers.IntegerField())

    def update(self, user_id, validated_data):
        return Profile.objects.filter(user__id=user_id).update(**validated_data)
