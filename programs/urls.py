from django.conf.urls import url, include
from rest_framework import routers
from programs.views import (
    WorkoutViewSet, ProgramViewSet, SetViewSet
)

workouts_router = routers.DefaultRouter()
workouts_router.register(r'workouts', WorkoutViewSet)

programs_router = routers.DefaultRouter()
programs_router.register(r'programs', ProgramViewSet)

sets_router = routers.DefaultRouter()
sets_router.register(r'sets', SetViewSet)

urlpatterns = [
    url(r'^', include(workouts_router.urls)),
    url(r'^', include(programs_router.urls)),
    url(r'^', include(sets_router.urls))
]
