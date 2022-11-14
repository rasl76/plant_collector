# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Plant, Light
from .forms import DebugForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

  # Add new view
@login_required
def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', { 'plants': plants })

@login_required
def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
    # Get the lights the plant doesn't have
  lights_plant_doesnt_have = Light.objects.exclude(id__in = plant.lights.all().values_list('id'))
  debug_form = DebugForm()
  return render(request, 'plants/detail.html', { 
    'plant': plant, 'debug_form': debug_form,
    # Add the lights to be displayed
    'lights': lights_plant_doesnt_have
    })

# add this new function below cats_detail
@login_required
def add_debug(request, plant_id):
  # create a ModelForm instance using the data in request.POST
  form = DebugForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_debug = form.save(commit=False)
    new_debug.plant_id = plant_id
    new_debug.save()
  return redirect('detail', plant_id=plant_id)

@login_required
def assoc_light(request, plant_id, light_id):
  Plant.objects.get(id=plant_id).lights.add(light_id)
  return redirect('detail', plant_id=plant_id)

@login_required
def unassoc_light(request, plant_id, light_id):
  Plant.objects.get(id=plant_id).lights.remove(light_id)
  return redirect('detail', plant_id=plant_id)

# View Class
class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = '__all__'
  success_url = '/plants/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['species', 'description', 'age']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

class LightList(LoginRequiredMixin, ListView):
  model = Light

class LightDetail(LoginRequiredMixin, DetailView):
  model = Light

class LightCreate(LoginRequiredMixin, CreateView):
  model = Light
  fields = '__all__'

class LightUpdate(LoginRequiredMixin, UpdateView):
  model = Light
  fields = ['name', 'lumen']

class LightDelete(LoginRequiredMixin, DeleteView):
  model = Light
  success_url = '/lights/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


