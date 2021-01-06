from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gamemode', views.choosemode),
    path('creategame', views.creategame),
    path('login', views.login),
    path('roomspage', views.roomspage),
    path('roomspageforuser', views.roomspageforuser),
    path('room', views.room),
    path('signup', views.signup),
    path('enterroom', views.enterroom),



]