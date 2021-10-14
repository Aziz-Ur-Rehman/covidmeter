from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r"", views.UserScenarioViewSet)

app_name = "scenario"
urlpatterns = [
    path("", include(router.urls)),
]
