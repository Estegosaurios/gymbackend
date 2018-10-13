from django.conf.urls import url, include
from rest_framework import routers
from programs.views import (
    WorkoutViewSet, ProgramViewSet, SetViewSet,
    ExercisesViewSet, ExercisesInSetViewSet
)

workouts_router = routers.DefaultRouter()
workouts_router.register(r'workouts', WorkoutViewSet)

programs_router = routers.DefaultRouter()
programs_router.register(r'programs', ProgramViewSet)

sets_router = routers.DefaultRouter()
sets_router.register(r'sets', SetViewSet)

exercises_router = routers.DefaultRouter()
exercises_router.register(r'exercises', ExercisesViewSet)

exercises_in_sets_router = routers.DefaultRouter()
exercises_in_sets_router.register(r'exercises_in_sets', ExercisesInSetViewSet)

urlpatterns = [
    url(r'^', include(workouts_router.urls)),
    url(r'^', include(programs_router.urls)),
    url(r'^', include(sets_router.urls)),
    url(r'^', include(exercises_router.urls)),
    url(r'^', include(exercises_in_sets_router.urls))
]
