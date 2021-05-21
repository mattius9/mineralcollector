from django.contrib import admin
from .models import Mineral, Viewing, Tool

# Register your models here.

admin.site.register(Mineral)
admin.site.register(Viewing)
admin.site.register(Tool)