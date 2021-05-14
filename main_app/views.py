from django.shortcuts import render
from django.views.generic import ListView
from .models import Mineral



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def minerals_index(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})

def minerals_detail(request, mineral_id):
    mineral = Mineral.objects.get(id=mineral_id)
    return render(request, 'minerals/detail.html', {'mineral':mineral})