from .views import EmailViewSet
from rest_framework import routers, urlpatterns
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'emails', EmailViewSet)

urlpatterns = [
    path('', include(router.urls))
]
