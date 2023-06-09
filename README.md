# Fitness Tracker App

This Fitness Tracker App aims to provide users with a seamless experience for creating and managing their workout routines. After logging in, users will land on a dashboard that displays a weekly schedule with the muscle groups targeted each day. Users can add or edit workout routines for each day, with each routine consisting of specific exercises pulled from the wger API. Users can also log their personal records for each exercise and automatically track improvements over time. Additional features include automatic updating of personal records and restrictions on assigning the same day to multiple routines.

## Technologies Used

- Python: The primary programming language used for writing the server-side logic.
- Django: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- PostgreSQL: An advanced open-source relational database used for data storage.
- wger API: A REST API that provides extensive exercise information for workout management.
- Free Inspirational Quote API by FreeCodeCamp: Provides motivational quotes to keep users inspired in their fitness journey.
- HTML, CSS, and JavaScript: for creating and styling the user interface.
- Heroku: A cloud platform used for deploying the web application.

## Getting Started

1. [Click here to access the Fitness Tracker App.](https://fittrax.herokuapp.com/accounts/login/?next=/)

2. https://trello.com/b/UrEJ3fEv/capstone-project
   
![Login](/screenshots/Login.png "Login")

3. Log in or sign up to access your personalized workout dashboard.

![Dashboard](/screenshots/home.png "Dashboard")

4. Once logged in, you will land on a dashboard that displays a weekly schedule with the muscle groups targeted each day.

![RoutineEditor](/screenshots/AddRoutine.png "RoutineEditor")

5. Click the button to add a new routine. Each routine consists of a name and the day of the week.

![Routines](/screenshots/Routines.png "Routines")
 
6. After submitting, you will be redirected back to the dashboard. Click on 'View Routies' to see routines, and associated exercises.

![ExerciseSearch1](/screenshots/Exercise-search1.png "ExerciseSearch1")

![ExerciseSearch](/screenshots/Exercise-Search.png "ExerciseSearch")

7. Search for the wanted exercise, and click on the name.

![AddExercise](/screenshots/Add-exercise.png "AddExercise")

8. Input necessary set and repetition information. After submitting, you'll be redirected to 'My Routines'.

![InspirationalQuote](/screenshots/Quote.png "InspirationalQuote")

9. Stay motivated with inspirational quotes fetched from the Free Inspirational Quote API by FreeCodeCamp.

## ICEBOX FEATURES

- Allow users to Edit and Delete Routines/Exercises
- Allow users to make logs of their workouts and track user improvement
- Allow users to see images of their selected workout, as well as necessary equipment and targeted muscles
- Allow users to share their workout routines with friends.
- Provide workout recommendations based on user's fitness goals.


### Pull Requests

I welcome pull requests for bug fixes, improvements, or new features. To contribute code to the project, follow these steps:

1. Fork the repository and create your branch from `main`.
2. Ensure your code follows the project's coding conventions and style guide.
3. Include tests to ensure the correctness of your changes.
4. Make sure your code passes all existing tests.
5. Write clear and concise commit messages.
6. Submit a pull request to the `main` branch.

I will review your pull request promptly.
