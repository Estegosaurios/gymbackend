from rest_framework import serializers
from programs.models import Workout, Program, Set, Exercises, ExercisesInSet


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'name', 'sets')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'workouts')


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('id', 'times', 'workout', 'ExercisesInSet')


class ExercisesSerializaer(serializers.ModelSerializer):
    model = Exercises
    fields = ('id', 'name')


class ExercisesInSetSerializer(serializers.ModelSerializer):
    model = ExercisesInSet
    fields = ('id', 'reps', 'duration')
