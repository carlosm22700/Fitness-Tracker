from django import forms
from .models import Routine, PlannedExercise


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'days_of_week']
        widgets = {
            'days_of_week': forms.SelectMultiple(attrs={'class': 'browser-default'})
        }


class PlannedExerciseForm(forms.ModelForm):
    class Meta:
        model = PlannedExercise
        fields = ['sets', 'reps']

# class PlannedExerciseForm(forms.ModelForm):
#     class Meta:
#         model = PlannedExercise
#         fields = ['routine', 'exercises', 'sets', 'reps']
