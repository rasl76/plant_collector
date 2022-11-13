# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import DebugForm

# Add the following import
from django.http import HttpResponse

# Add the Plant class & list and view function below the imports
# class Plant:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, species, description, age):
#     self.name = name
#     self.species = species
#     self.description = description
#     self.age = age

# plants = [
#   Plant('Charles', 'Christmas Cactus', 'foul little demon', 3),
#   Plant('William', 'Hoya', 'Still waiting to flower',4),
#   Plant('Harry', 'Pothos', 'Can survive under harsh conditions', 4)
# ]


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
  debug_form = DebugForm()
  return render(request, 'plants/detail.html', { 
    'plant': plant, 'debug_form': debug_form 
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

