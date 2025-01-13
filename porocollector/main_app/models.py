from django.db import models
from django.urls import reverse

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

class Poro(models.Model):
    name= models.CharField(max_length=100)
    region= models.CharField(max_length=100, choices=REGIONS)
    description= models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'poro_id':self.id})
    
    def __str__(self):
        return self.name