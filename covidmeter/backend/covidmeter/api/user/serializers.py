from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.covid.serializers import CountrySerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`user.User`.
    """

    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]
        read_only_fields = (
            "is_active",
            "is_staff",
            "is_superuser",
        )
        extra_kwargs = {"password": {"write_only": True}}


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`user.User`.
    """

    country = CountrySerializer()

    class Meta:
        model = User
        exclude = ("password", "user_permissions", "groups")
