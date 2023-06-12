import requests
from main_app.models import Exercise
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetches data from the API and stores it in the database'

    def handle(self, *args, **kwargs):
        base_url = 'https://wger.de/api/v2/exercise/'
        page_url = base_url

        while page_url:
            # Make an API request
            response = requests.get(page_url)

            # Check if the request was successful
            if response.status_code == 200:
                response_data = response.json()

                # Loop through each item in the response
                for exercise in response_data['results']:
                    muscle_group = ''

                    # Create a new Exercise object and save it to the database
                    Exercise.objects.get_or_create(
                        api_id=exercise['id'],
                        defaults={
                            'name': exercise['name'],
                            'description': exercise['description'],
                            'muscle_group': muscle_group,
                            'image_url': exercise.get('image') or 'default_image_url'
                        }
                    )

                # Get the next page URL
                page_url = response_data.get('next')
            else:
                self.stdout.write(self.style.ERROR(
                    'Failed to fetch data from the API'))
                break

        self.stdout.write(self.style.SUCCESS(
            'Data successfully saved to the database'))
