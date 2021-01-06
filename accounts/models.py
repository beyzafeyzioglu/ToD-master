from django.db import models


class UnRegPlayer (models.Model):
    gender = models.CharField(max_length=10, default="")
    nickname = models.CharField(max_length=100, default="")


class RegPlayer(models.Model):
    nickname = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=10, default="")
    age = models.IntegerField(null=True)
    mail = models.EmailField(max_length=150)
    password = models.CharField(max_length=8, default="")


class Room(models.Model):
    roomCode = models.CharField(max_length=100, default="")
    roomName = models.CharField(max_length=100, default="")
    status = models.BooleanField()
    numOfPlayers = models.IntegerField(null=True)
    genderPref = models.CharField(max_length=10, default="")