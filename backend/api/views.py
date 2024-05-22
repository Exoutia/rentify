from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Property, UserProfile
from .serializers import PropertySerializer, UserProfileSerializer, UserSerializer


@extend_schema(tags=["Auth"])
class RegisterUserProfile(APIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_profile = serializer.save()
            return Response(
                {
                    "user_profile": UserProfileSerializer(user_profile).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Profiles"])
class UserProfiesListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=["Profiles"])
class UserProfileRetrieveView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=["Properties"])
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=["Properties"])
class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
