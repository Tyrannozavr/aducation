from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')


def register(request):
    if request.POST:
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('password')
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'authentication/register.html', {'message': 'username is already taken'})
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'authentication/register.html')


def login_view(request):
    if request.POST:
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'authentication/login.html', {'message': 'Invalid username or password'})
        else:
            login(request, user)
            return redirect(reverse('testing-list'))
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('testing-list'))
