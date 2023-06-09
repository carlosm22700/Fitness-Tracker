import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RoutineForm
from .models import TrainingDay

# Create your views here.


@login_required
def home(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
    return render(request, 'main_app/home.html', {'days_of_week': days_of_week})


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
    # user us navigating to signup page to fill out the form


def add_routine(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RoutineForm()
    return render(request, 'main_app/add_routine.html', {'form': form})


def exercise_search(request):
    query = request.GET.get('query')

    # Only proceed if there is a query
    if query:
        # Use the exercise_search_retrieve endpoint
        search_url = 'https://wger.de/api/v2/exercise/search/'

        # Parameters for the search: language and term
        params = {
            'language': '2',  # Assuming 2 is for English
            'term': query
        }

        # Output the full URL and parameters
        print(f"URL: {search_url}, Parameters: {params}")

        # Make the request to the API
        response = requests.get(search_url, params=params)

        # Check if the response is successful
        if response.status_code == 200:
            response_data = response.json()

            # Extract the suggestions from the response
            suggestions = response_data.get('suggestions', [])

            # Extract the exercise data from the suggestions
            exercises = [suggestion['data'] for suggestion in suggestions]

            base_image_url = "https://wger.de"

            # Replace None images with a placeholder image and prepend base URL to image paths
            for exercise in exercises:
                if exercise['image'] is None:
                    # or a URL to a default image
                    exercise['image'] = 'https://boxlifemagazine.com/wp-content/uploads/2023/04/image-7-1-e1680703796192.jpeg'
                else:
                    exercise['image'] = f"{base_image_url}{exercise['image']}"

            # Render the template with the exercise data
            return render(request, 'main_app/exercise_search.html', {'exercises': exercises})

        # If the response is not successful, render an error page
        return render(request, 'error.html', {'message': 'Could not retrieve exercises.'})

    # If there is no query, just render the search page without results
    return render(request, 'main_app/exercise_search.html')
