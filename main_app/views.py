from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Mineral, Tool
from .forms import ViewingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class MineralCreate(LoginRequiredMixin, CreateView):
    model = Mineral
    fields = ['name', 'm_class', 'colour', 'hardness']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MineralUpdate(LoginRequiredMixin, UpdateView):
    model = Mineral
    fields = ['m_class', 'colour', 'hardness']

class MineralDelete(LoginRequiredMixin, DeleteView):
    model = Mineral
    success_url = '/minerals/'




# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def minerals_index(request):
    minerals = request.user.mineral_set.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})

@login_required
def minerals_detail(request, mineral_id):
    mineral = Mineral.objects.get(id=mineral_id)
    tools_not_associated = Tool.objects.exclude(id__in = mineral.tools.all().values_list('id'))
    viewing_form = ViewingForm()
    return render(request, 'minerals/detail.html', {
        'mineral':mineral, 'viewing_form': viewing_form, 'tools' : tools_not_associated
    })

@login_required
def add_viewing(request, mineral_id):
    form = ViewingForm(request.POST)
    if form.is_valid():
        new_viewing = form.save(commit=False)
        new_viewing.mineral_id = mineral_id
        new_viewing.save()
    return redirect('detail', mineral_id=mineral_id)

class ToolList(LoginRequiredMixin, ListView):
    model = Tool

class ToolDetail(LoginRequiredMixin, DetailView):
    model = Tool

class ToolCreate(LoginRequiredMixin, CreateView):
    model = Tool
    fields = '__all__'

class ToolDelete(LoginRequiredMixin, DeleteView):
    model = Tool
    success_url = '/tools'

class ToolUpdate(LoginRequiredMixin, UpdateView):
    model = Tool
    fields = ['name', 'brand']

@login_required
def assoc_tool(request, mineral_id, tool_id):
    Mineral.objects.get(id=mineral_id).tools.add(tool_id)
    return redirect('detail', mineral_id=mineral_id)

@login_required
def unassoc_tool(request, mineral_id, tool_id):
    Mineral.objects.get(id=mineral_id).tools.remove(tool_id)
    return redirect('detail', mineral_id=mineral_id)

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)