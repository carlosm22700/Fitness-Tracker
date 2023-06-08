import requests
from django.shortcuts import render
from urllib.parse import quote

# Create your views here.


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
