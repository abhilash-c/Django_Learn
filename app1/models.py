from django.db import models

# Create your models here.
class detail:
    name:str
    age:int
    place:str
    email:str

class stud(models.Model):
    name= models.CharField(max_length=255)
    adress = models.CharField(max_length=255)