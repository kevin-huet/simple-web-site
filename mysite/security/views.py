from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        #login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect('index')
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('index')

