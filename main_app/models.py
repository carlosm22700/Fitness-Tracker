from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exercise(models.Model):
    api_id = models.IntegerField(null=True, default=None)
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle_group = models.CharField(max_length=200)
    image_url = models.URLField()

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=200)
    days_of_week = models.ManyToManyField(TrainingDay)

    def __str__(self):
        return f'Routine {self.name} for {self.user.username}'


class PlannedExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f'Planned exercise in routine {self.routine}'


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)

    def __str__(self):
        return f'Log for {self.user.username} on {self.date}'
