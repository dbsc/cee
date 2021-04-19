from django.urls import include, path
from rest_framework import routers
from .views import (
    FieldViewSet, PositionViewSet, RequirementViewSet,
    SimpleVacancyViewSet, VacancyViewSet
)

router = routers.DefaultRouter()
router.register(r'vacancies', VacancyViewSet)
router.register(r'simplevacancies', SimpleVacancyViewSet)
router.register(r'requirements', RequirementViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'positions', PositionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
