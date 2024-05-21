from django.urls import path

from .views import (
    PropertyListCreateView,
    PropertyRetrieveUpdateDestroyView,
    UserProfiesListView,
    UserProfileRetrieveView,
)

urlpatterns = [
    path("users/", UserProfiesListView.as_view(), name="user-profiles-list"),
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
