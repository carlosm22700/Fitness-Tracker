from django.contrib import admin

from .models import Exercise, TrainingDay, Routine, Log, PlannedExercise
# Register your models here.
admin.site.register(Exercise)
admin.site.register(TrainingDay)
admin.site.register(PlannedExercise)
admin.site.register(Routine)
admin.site.register(Log)
