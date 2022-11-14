from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PESTICIDES = (
    ('F', 'Fungicide'),
    ('I', 'Insecticide'),
    ('H', 'Herbicide')
)

class Light(models.Model):
  name = models.CharField(max_length=50)
  lumen = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lights_detail', kwargs={'pk': self.id})

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Add the M:M relationship
    lights = models.ManyToManyField(Light)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

    # would need to filter it for  month
    # def debugged_for_month(self):
    #     return self.debug_set.filter(date=date.today()).count() >= len(PESTICIDES)

# Add new Do model below Cat model
class Debug(models.Model):
  date = models.DateField('debug date')
  dose = models.CharField(max_length=1)
  pesticide = models.CharField(max_length=1,
    # add the 'choices' field option
    choices=PESTICIDES,
    # set the default value for meal to be 'B'
    default=PESTICIDES[0]
    )
  # Create a plant_id FK
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_pesticide_display()} on {self.date}"
  class Meta:
    ordering = ['-date']