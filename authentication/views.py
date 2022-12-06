from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse('hello, authentication')


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
    return render(request, 'authentication/login.html')
