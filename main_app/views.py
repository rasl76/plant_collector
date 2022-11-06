# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Plant class & list and view function below the imports
class Plant:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

plants = [
  Plant('Charles', 'Christmas Cactus', 'foul little demon', 3),
  Plant('William', 'Hoya', 'Still waiting to flower',4),
  Plant('Harry', 'Pothos', 'Can survive under harsh conditions', 4)
]


# Define the home view
def home(request):
  return HttpResponse('<h1>:)</h1>')

def about(request):
  return render(request, 'about.html')

  # Add new view
def plants_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })
