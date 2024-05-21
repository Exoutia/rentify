from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Property, UserProfile


# TODO: Create a user serializer and implement the registration and login logic
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
