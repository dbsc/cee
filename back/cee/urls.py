from allauth.socialaccount import adapter
from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from rest_framework.schemas import get_schema_view as drf_get_schema_view

from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi

drf_schema_view = drf_get_schema_view(
    title="CEE API",
    description="API for the CEE Website",
    version="v1",
)

yasg_schema_view = yasg_get_schema_view(
    openapi.Info(
        title="CEE API",
        default_version="v1",
        description="API for the CEE Website",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', include('vacancies.urls')),
    path('companies/', include('companies.urls')),
    path('events/', include('events.urls')),
    path('social/', include('social.urls')),
    path('emails/', include('emails.urls')),
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('redoc/', yasg_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('openapi/', drf_schema_view, name='schema-openapi'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
