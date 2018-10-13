from django.contrib import admin
from programs.models import (
    Workout, Program, Set, Exercises, ExercisesInSet
)

admin.site.register(Workout)
admin.site.register(Program)
admin.site.register(Set)
admin.site.register(Exercises)
admin.site.register(ExercisesInSet)
