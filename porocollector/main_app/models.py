from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

REGIONS = (
    ('F','Freljord'),
    ('D','Demacia'),
    ('I','Ionia'),
    ('N','Noxus'),
    ('P','Piltover & Zaun'),
    ('S','Shadow Isles'),
    ('B','Bilgewater'),
    ('T','Targon'),
    ('SH','Shurima'),
    ('BC','Bandle City'),
    ('R','Runterra')
)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('toys_detail', kwargs={'pk': self.id})

class Poro(models.Model):
    name= models.CharField(max_length=100)
    region= models.CharField(max_length=100, choices=REGIONS, default=REGIONS[0][0])
    description= models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'poro_id':self.id})
    
    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >=3  
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices= MEALS, default=MEALS[0][0])
    poro = models.ForeignKey(Poro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date} for {self.poro}'