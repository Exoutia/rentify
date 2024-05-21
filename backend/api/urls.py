from django.urls import path

from .views import (
    PropertyListCreateView,
    PropertyRetrieveUpdateDestroyView,
    RegisterUserProfile,
    UserProfiesListView,
    UserProfileRetrieveView,
)

urlpatterns = [
    path("users/", UserProfiesListView.as_view(), name="user-profiles-list"),
    path("register/", RegisterUserProfile.as_view(), name="register-user"),
    path(
        "users/<int:pk>",
        UserProfileRetrieveView.as_view(),
        name="user-retrieve",
    ),
    path("properties/", PropertyListCreateView.as_view(), name="property-list-create"),
    path(
        "properties/<int:pk>/",
        PropertyRetrieveUpdateDestroyView.as_view(),
        name="property-retrieve-update-destroy",
    ),
]
