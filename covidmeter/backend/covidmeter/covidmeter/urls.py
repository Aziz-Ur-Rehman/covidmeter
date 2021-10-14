import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.user.views import LogoutFromAllDevicesView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # django debugger
    path("__debug__/", include(debug_toolbar.urls)),
    # jwt
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/logoutall/", LogoutFromAllDevicesView.as_view(), name="logout-all"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
