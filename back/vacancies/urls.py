from django.urls import include, path
from rest_framework import routers, urlpatterns
from .views import VacancyViewSet

router = routers.DefaultRouter()
router.register(r'vancancies', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
