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


class Set(BaseModel):
    times = models.IntegerField()
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='sets'
    )
