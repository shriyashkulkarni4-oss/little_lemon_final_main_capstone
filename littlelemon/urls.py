from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from restaurant.views import RegisterView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/token/", obtain_auth_token, name="api-token"),
    path("api-auth/", include("rest_framework.urls")),
]
