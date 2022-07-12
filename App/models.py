from django.db import models

# Create your models here

class signUp(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    age = models.DurationField()
    gender = models.TextField()
    password = models.TextField()
    course = models.TextField()
    time = models.TextField()