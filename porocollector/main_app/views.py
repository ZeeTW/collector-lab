from django.shortcuts import render
from django.http import HttpResponse
from .models import Poro
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PoroCreate(CreateView):
    model = Poro
    fields = '__all__'

class PoroUpdate(UpdateView):
    model = Poro
    fields = '__all__'

class PoroDelete(DeleteView):
    model = Poro
    success_url = '/poros/'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def poro_index(request):
    poros = Poro.objects.all()
    return render(request, 'poros/index.html', {'poros': poros})

def poros_detail(request, poro_id):
    poro = Poro.objects.get(id = poro_id)
    feeding_form = FeedingForm()
    return render(request, 'poros/detail.html', {'poro' : poro})

