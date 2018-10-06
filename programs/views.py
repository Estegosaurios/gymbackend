from django.shortcuts import render
from rest_framework import viewsets
from programs.models import Workout
from programs.serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
