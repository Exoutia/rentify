from django.urls import path

from .views import (
    OwnerListCreateView,
    OwnerRetrieveUpdateDestroyView,
    PropertyListCreateView,
    PropertyRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("owners/", OwnerListCreateView.as_view(), name="owner-list-create"),
    path(
        "owners/<int:pk>/",
        OwnerRetrieveUpdateDestroyView.as_view(),
        name="owner-retrieve-update-destroy",
    ),
    path("properties/", PropertyListCreateView.as_view(), name="property-list-create"),
    path(
        "properties/<int:pk>/",
        PropertyRetrieveUpdateDestroyView.as_view(),
        name="property-retrieve-update-destroy",
    ),
]
