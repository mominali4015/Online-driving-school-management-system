from os import name
from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.TextField()
    
