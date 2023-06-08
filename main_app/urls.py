from django.urls import path
from . import views
# from .views import register, login_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('exercise_search/', views.exercise_search, name='exercise_search'),
]

# path('accounts/register/', register, name='register'),
# path('accounts/login/', login_view, name='login'),
# path('accounts/logout/', logout_view, name='logout'),
