from django.contrib import admin
from .models import Vacancy, SimpleVacancy, Requirement, Field, Position


admin.site.register([
    Vacancy, SimpleVacancy, Requirement, Field, Position
])
