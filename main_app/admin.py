from django.contrib import admin

from .models import Exercise, Workout, TrainingDay, TrainingData, Routine, Log
# Register your models here.
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(TrainingDay)
admin.site.register(TrainingData)
admin.site.register(Routine)
admin.site.register(Log)
