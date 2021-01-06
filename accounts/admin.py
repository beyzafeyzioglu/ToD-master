from django.contrib import admin

from django.contrib import admin
from .models import Room
from .models import UnRegPlayer
from .models import RegPlayer
admin.site.register(Room)
admin.site.register(UnRegPlayer)
admin.site.register(RegPlayer)
