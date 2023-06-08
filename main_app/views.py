import requests
from django.shortcuts import render
from urllib.parse import quote

# Create your views here.
'''
TODO:
*Work on Workout & Routine implementation and link to auth sessions in models
*work on log implementaion and PRs
-AAU, I want to see a list of Routine split up into days of the week when looking at my dash/home page
-each routine 'day' displays the days of the week on the left and to the right of each day, the 'title' of the split e.g chest/tris, or upper body. this is based on a user input.
-AAU, when I click on a 'workout' link at the top of the chart, i want to see a display of each individual routine and its exercises ive added so far. if empty it displays "no exercises added'.
-AAU, I want to add workouts/exercises for each routine by clicking on a plus logo. When doing this, it would take me to the exersice, search page.
-AAU, when I reach the search page, I want to be able to search for exercises and each exercise should display a button that adds it to my workout list, under the specific routine that I added. I will then be redirected back to my workout page to see the workout added under the specific routine.
-AAU, I should be able to delete a specific exercise associated with the routine, from the workouts page.
-AAU, when clicking on the ADD WORKOUT button I want to be able to create a name for the Workout/Routine, and assign the given days of the week for that routine using a checkbox. If another workout is already using that specific day of thew week, it should not appear as an option.
-AAU, when saving a new routine/workout I want to be able to be redirected to my workouts page with the new routine added. From there I can add exercises to that routine as needed
'''


def home(request):
    return render(request, 'main_app/home.html')


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
