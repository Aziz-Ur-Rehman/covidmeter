from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("", views.UserListCreateView.as_view(), name="user-list-create"),
    path(
        "<int:pk>/",
        views.UserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
    path(
        "profile/",
        views.UserProfileView.as_view(),
        name="user-profile",
    ),
]
