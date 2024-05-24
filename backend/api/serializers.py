from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Property, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                password=validated_data["password"],
            )
            return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ["user", "phone_number", "bio"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        new_user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"],
        )
        user_profile = UserProfile.objects.create(
            user=new_user,
            phone_number=validated_data["phone_number"],
            bio=validated_data["bio"],
        )
        user_profile.save()
        return user_profile


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(username=attrs["username"])
        user_profile = UserProfile.objects.get(user=user)

        # Add custom claims
        data["owner_id"] = user_profile.id

        return data
