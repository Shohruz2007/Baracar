from django.contrib import admin
from .models import CustomUser, Adress

admin.site.register(CustomUser)
admin.site.register(Adress)