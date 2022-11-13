from django.db import models
from django.urls import reverse

PESTICIDES = (
    ('F', 'Fungicide'),
    ('I', 'Insecticide'),
    ('H', 'Herbicide')
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

# Add new Do model below Cat model
class Debug(models.Model):
  date = models.DateField()
  dose = models.CharField(max_length=1)
  pesticide = models.CharField(
    max_length=100,
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