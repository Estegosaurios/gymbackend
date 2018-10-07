from rest_framework import serializers
from programs.models import Workout, Program, WorkoutInProgram


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'name')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'workouts_in_program')


class WorkoutInProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutInProgram
        fields = ('id', 'date', 'program', 'workout')
