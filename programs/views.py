from django.shortcuts import render
from rest_framework import viewsets
from programs.models import Workout, Program, WorkoutInProgram
from programs.serializers import (
    WorkoutSerializer, ProgramSerializer, WorkoutInProgramSerializer
)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class WorkoutInProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutInProgram.objects.all()
    serializer_class = WorkoutInProgramSerializer
