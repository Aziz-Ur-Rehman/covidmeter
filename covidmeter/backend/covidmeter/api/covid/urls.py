from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"report", views.ReportViewset)
router.register(r"continent", views.ContinentViewset)
router.register(r"country", views.CountryViewset)

app_name = "covid"
urlpatterns = [
    path("", include(router.urls)),
    path("graph/", views.GraphApiView.as_view()),
    path("graph/country/<str:geoid>", views.GraphApiView.as_view()),
    path("graph/continent/<str:continent>", views.GraphApiView.as_view()),
]
