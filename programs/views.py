from django.shortcuts import render
from rest_framework import viewsets
from programs.models import Workout, Program, Set
from programs.serializers import (
    WorkoutSerializer, ProgramSerializer, SetSerializer
)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
