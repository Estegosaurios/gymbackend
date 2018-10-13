from django.db import models
from core.models import BaseModel


class Workout(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(BaseModel):
    name = models.CharField(max_length=100)
    workouts = models.ManyToManyField(Workout)

    def __str__(self):
        return self.name


class Exercises(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Set(BaseModel):
    times = models.IntegerField()
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='sets'
    )
    exercises = models.ManyToManyField(
        Exercises,
        through='ExercisesInSet',
        through_fields=('workout_set', 'exercise')
    )

    def __str__(self):
        return u'{times}'.format(
            times=self.times
        )


class ExercisesInSet(BaseModel):
    workout_set = models.ForeignKey(
        Set,
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercises,
        on_delete=models.CASCADE
    )
    reps = models.IntegerField()
    duration = models.IntegerField()
