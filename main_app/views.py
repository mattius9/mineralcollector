from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Temporary Dataset

class Mineral:
    def __init__(self,name,m_class,colour,hardness,magnetic=False):
        self.name = name
        self.m_class = m_class
        self.colour = colour
        self.hardness = hardness
        self.magnetic = magnetic

minerals = [
    Mineral('Amethyst', 'tectosilicate', 'violet', 7 ),
    Mineral('Pyrite', 'sulfide', 'brass', 6),
    Mineral('Cinnabar', 'sulfide', 'brown-red', 2),
    Mineral('Chromite', 'oxide', 'brown-black',5.5 ,True)
]


def home(request):
    return HttpResponse('<h1>Hello ¯\_( ツ )_/¯ <h1>')

def about(request):
    return render(request, 'about.html')

def minerals_index(request):
    return render(request, 'minerals/index.html', {'minerals': minerals})