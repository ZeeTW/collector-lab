from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poro, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class PoroCreate(LoginRequiredMixin, CreateView):
    model = Poro
    # fields = '__all__'
    fields = ['name', 'region', 'description', 'image']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PoroUpdate(UpdateView):
    model = Poro
    fields = ['name', 'description', 'image']

class PoroDelete(DeleteView):
    model = Poro
    success_url = '/poros/'
    
class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
    #can write __all__ ^^

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def poro_index(request):
    poros = Poro.objects.filter(user=request.user)
    return render(request, 'poros/index.html', {'poros': poros})

@login_required
def poros_detail(request, poro_id):
    poro = Poro.objects.get(id = poro_id)
    feeding_form = FeedingForm()
    toys_poro_doesnt_have = Toy.objects.exclude(id__in = poro.toys.all().values_list('id'))
    return render(request, 'poros/detail.html',{'poro':poro, 'feeding_form' : feeding_form, 'toys' : toys_poro_doesnt_have})

@login_required
def add_feeding(request, poro_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit = False)
        new_feeding.poro_id = poro_id
        new_feeding.save()

    return redirect('detail', poro_id = poro_id)

@login_required
def assoc_toy(request, poro_id, toy_id):
    print("poro_id, toy_id", poro_id, toy_id)
    Poro.objects.get(id = poro_id).toys.add(toy_id)
    return redirect('detail', poro_id = poro_id)

@login_required
def unassoc_toy(request, poro_id, toy_id):
    Poro.objects.get(id = poro_id).toys.remove(toy_id)
    return redirect('detail', poro_id = poro_id)


def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index')
        
        else:
            error_message = 'Invalid Sign-up please try again later.'

    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)