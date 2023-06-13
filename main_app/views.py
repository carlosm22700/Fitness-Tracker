from django.contrib import messages
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login
from .forms import RoutineForm, PlannedExerciseForm
from .models import TrainingDay, Routine, Exercise, PlannedExercise

# Create your views here.


@login_required
def home(request):
    days_of_week = TrainingDay.objects.all()
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'main_app/home.html', {'days_of_week': days_of_week, 'routines': routines})


def signup(request):
    # POST request
    error_message = ''
    # user is signing up with a form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid signup - try again'
    # GET request
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })
    # user is navigating to signup page to fill out the form


@login_required
def view_routines(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'main_app/view_routines.html', {'routines': routines})


@login_required
def add_routine(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            selected_days = form.cleaned_data.get('days_of_week')
            # Check if routine already exists for selected days
            for day in selected_days:
                if Routine.objects.filter(user=request.user, days_of_week=day).exists():
                    messages.error(
                        request, f'Routine already exists for {day}.')
                    # or render the form again with an error message
                    return redirect('add_routine')
            # Save the routine if no conflicts
            routine = form.save(commit=False)
            routine.user = request.user
            routine.save()
            form.save_m2m()  # save the many-to-many relationship with TrainingDay
            return redirect('home')
    else:
        form = RoutineForm()
    return render(request, 'main_app/add_routine.html', {'form': form})


@login_required
def add_exercise(request, routine_id, exercise_id):
    routine = get_object_or_404(Routine, id=routine_id)
    selected_exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == 'POST':
        form = PlannedExerciseForm(request.POST)
        if form.is_valid():
            planned_exercise = form.save(commit=False)
            planned_exercise.routine = routine
            planned_exercise.exercise = selected_exercise
            planned_exercise.save()
            return redirect('view_routines')
    else:
        # Set initial data for the form
        form = PlannedExerciseForm(initial={'exercise': selected_exercise})
    return render(request, 'main_app/add_exercise.html', {'form': form, 'routine': routine, 'selected_exercise': selected_exercise, 'selected_exercise_id': exercise_id})


@login_required
def exercise_search(request, routine_id):
    query = request.GET.get('query')
    exercises = []
    if query:
        exercises = Exercise.objects.filter(name__icontains=query)
    return render(request, 'main_app/exercise_search.html', {'exercises': exercises, 'routine_id': routine_id})


@require_http_methods(["POST"])
def delete_routine(request, routine_id):
    try:
        routine = Routine.objects.get(pk=routine_id)
        routine.delete()
    except Routine.DoesNotExist:
        pass  # handle the case where the routine does not exist if needed
    return redirect('view_routines')


@require_http_methods(["POST"])
def delete_exercise(request, routine_id, exercise_id):
    try:
        planned_exercise = PlannedExercise.objects.get(
            pk=exercise_id, routine__id=routine_id)
        planned_exercise.delete()
    except PlannedExercise.DoesNotExist:
        pass
    return redirect('view_routines')
