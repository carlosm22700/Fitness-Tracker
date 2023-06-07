from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'main_app/home.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')
