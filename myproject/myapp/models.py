from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.cuisine}"
    
    
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    
