from django.urls import include, path
from rest_framework import routers
from .views import (
    FieldViewSet, LocationViewSet, PositionViewSet, RequirementViewSet,
    SimpleVacancyViewSet, VacancyViewSet, TagViewSet,
    ResponsibilityViewSet
)

router = routers.DefaultRouter()
router.register(r'vacancies', VacancyViewSet, basename='vacancies')
router.register(r'simplevacancies', SimpleVacancyViewSet)
router.register(r'requirements', RequirementViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'tags', TagViewSet)
router.register(r'responsibilities', ResponsibilityViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
