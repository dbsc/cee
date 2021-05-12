from django.urls import include, path
from rest_framework import routers
from .views import (
    FieldViewSet, PositionViewSet, RequirementViewSet,
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

urlpatterns = [
    path('', include(router.urls))
]
