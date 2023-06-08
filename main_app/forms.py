from django import forms
from .models import Routine, PlannedExercise


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'days_of_week']


class PlannedExerciseForm(forms.ModelForm):
    class Meta:
        model = PlannedExercise
        fields = ['routine', 'exercises', 'sets', 'reps']
