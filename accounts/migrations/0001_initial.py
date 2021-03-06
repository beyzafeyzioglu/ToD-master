# Generated by Django 3.1.4 on 2021-01-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('mail', models.EmailField(max_length=150)),
                ('password', models.CharField(default='', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomCode', models.CharField(default='', max_length=100)),
                ('roomName', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField()),
                ('numOfPlayers', models.IntegerField(null=True)),
                ('genderPref', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UnRegPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='', max_length=10)),
                ('nickname', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
