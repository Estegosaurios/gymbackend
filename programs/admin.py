from django.contrib import admin
from programs.models import Workout, Program, WorkoutInProgram

admin.site.register(Workout)
admin.site.register(Program)
admin.site.register(WorkoutInProgram)
