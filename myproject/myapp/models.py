from django.db import models

# Create your models here.

class Person(models.Model):
    lasat_name = models.TextField()
    first_name = models.TextField()
    
    def __str__(self):
        return f"{self.lasat_name} {self.first_name}"
