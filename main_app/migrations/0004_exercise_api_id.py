# Generated by Django 4.2.2 on 2023-06-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_plannedexercise_remove_workout_exercises_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='api_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]