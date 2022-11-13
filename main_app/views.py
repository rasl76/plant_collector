# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Light
from .forms import DebugForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

  # Add new view
def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', { 'plants': plants })

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

def assoc_light(request, plant_id, light_id):
  Plant.objects.get(id=plant_id).lights.add(light_id)
  return redirect('detail', plant_id=plant_id)

def unassoc_light(request, plant_id, light_id):
  Plant.objects.get(id=plant_id).lights.remove(light_id)
  return redirect('detail', plant_id=plant_id)

# View Class
class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['species', 'description', 'age']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

class LightList(ListView):
  model = Light

class LightDetail(DetailView):
  model = Light

class LightCreate(CreateView):
  model = Light
  fields = '__all__'

class LightUpdate(UpdateView):
  model = Light
  fields = ['name', 'lumen']

class LightDelete(DeleteView):
  model = Light
  success_url = '/lights/'


