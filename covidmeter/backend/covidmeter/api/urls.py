from django.urls import include, path


app_name = "api"
urlpatterns = [
    path("covid/", include("api.covid.urls")),
    path("scenario/", include("api.scenario.urls")),
    path("user/", include("api.user.urls")),
]
