from django.urls import include, path
from rest_framework import routers, urlpatterns
from .views import SimpleVacancyViewSet, VacancyViewSet

router = routers.DefaultRouter()
router.register(r'vancancies', VacancyViewSet)
router.register(r'simplevacancies', SimpleVacancyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
