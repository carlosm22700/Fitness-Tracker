from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercise_search/', views.exercise_search, name='exercise_search'),
    path('accounts/signup/', views.signup, name='signup'),
    path('add_routine/', views.add_routine, name='add_routine'),
]
