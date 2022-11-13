from django.forms import ModelForm
from .models import Debug

class DebugForm(ModelForm):
  class Meta:
    model = Debug
    fields = ['date', 'dose', 'pesticide']
