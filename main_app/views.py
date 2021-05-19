from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Mineral
from .forms import ViewingForm

class MineralCreate(CreateView):
    model = Mineral
    fields = '__all__'
    # fields = ['name', 'm_class', 'colour', 'hardness', 'magnetic']
    # success_url = '/minerals/'

class MineralUpdate(UpdateView):
    model = Mineral
    fields = ['m_class', 'colour', 'hardness', 'magnetic']

class MineralDelete(DeleteView):
    model = Mineral
    success_url = '/minerals/'




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
    viewing_form = ViewingForm()
    return render(request, 'minerals/detail.html', {
        'mineral':mineral, 'viewing_form': viewing_form
    })

def add_viewing(request, mineral_id):
    form = ViewingForm(request.POST)
    if form.is_valid():
        new_viewing = form.save(commit=False)
        new_viewing.mineral_id = mineral_id
        new_viewing.save()
    return redirect('detail', mineral_id=mineral_id)