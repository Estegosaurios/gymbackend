from django.db import models
from core.models import BaseModel


class Workout(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(BaseModel):
    name = models.CharField(max_lenght=100)
    workouts = models.ManyToManyField(
        Workout,
        through='WorkoutInProgram',
        through_fields=('program', 'workout'),
        related_name='programs'
    )

    def __str__(self):
        return self.name


class WorkoutInProgram(BaseModel):
    date = models.DateField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return u'{program}-{workout}. Date: {date}'.format(
            program=self.program.name,
            workout=self.workout.name,
            date=self.date
        )
