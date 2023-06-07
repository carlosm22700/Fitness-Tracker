from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle_group = models.CharField(max_length=200)
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f'Workout for {self.user.username}'


class TrainingData(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f'Training data for {self.workout}'


class TrainingDay(models.Model):
    DAY_CHOICES = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    )

    day = models.CharField(max_length=3, choices=DAY_CHOICES)

    def __str__(self):
        return self.day


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workouts = models.ManyToManyField(Workout)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'Routine {self.name} for {self.user.username}'


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    reps = models.IntegerField()
    weight = models.FloatField

    def __str__(self):
        return f'Log for {self.user.username} on {self.date}'
