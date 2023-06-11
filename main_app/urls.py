from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercise_search/<int:routine_id>/',
         views.exercise_search, name='exercise_search'),
    path('accounts/signup/', views.signup, name='signup'),
    path('add_routine/', views.add_routine, name='add_routine'),
    path('view_routines/', views.view_routines, name='view_routines'),
    path('add_exercise/<int:routine_id>/<int:exercise_id>/',
         views.add_exercise, name='add_exercise'),
    path('delete_routine/<int:routine_id>',
         views.delete_routine, name='delete_routine'),
    path('delete_exercise/<int:routine_id>/<int:exercise_id>',
         views.delete_exercise, name='delete_exercise'),

]
