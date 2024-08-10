from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from . import models


def index(request):
    profiles = models.Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'index.html', context)


@csrf_protect
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return  redirect('login')
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('index')


def profile(request):
    profiles = models.Profile.objects.all()
    context = {
        'profiles':profiles
    }
    return render(request, 'profile.html', context)