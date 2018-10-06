from django.conf.urls import url, include
from rest_framework import routers
from programs.views import WorkoutViewSet

workouts_router = routers.DefaultRouter()
workouts_router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    url(r'^', include(workouts_router.urls)),
]
