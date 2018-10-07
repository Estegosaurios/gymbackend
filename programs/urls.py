from django.conf.urls import url, include
from rest_framework import routers
from programs.views import WorkoutViewSet, ProgramViewSet

workouts_router = routers.DefaultRouter()
workouts_router.register(r'workouts', WorkoutViewSet)

programs_router = routers.DefaultRouter()
programs_router.register(r'programs', ProgramViewSet)

urlpatterns = [
    url(r'^', include(workouts_router.urls)),
    url(r'^', include(programs_router.urls)),
]
