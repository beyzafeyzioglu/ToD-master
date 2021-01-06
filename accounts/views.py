
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/home.html')


def choosemode(request):
    return render(request, 'accounts/gamemode.html')


def creategame(request):
    return render(request, 'accounts/creategame.html')


def login(request):
    return render(request, 'accounts/login.html')


def roomspage(request):
    return render(request, 'accounts/roomspage.html')


def roomspageforuser(request):
    return render(request, 'accounts/roomspageforuser.html')


def room(request):
    return render(request, 'accounts/room.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def enterroom(request):
    return render(request, 'accounts/enterroom.html')


