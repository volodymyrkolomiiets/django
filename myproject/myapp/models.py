from django.db import models

# Create your models here.

class Person(models.Model):
    ClientOwner = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
    Patronym = models.CharField(max_length=200, null=True)
    OtherInfo = models.CharField(max_length=200, null=True)
    BirthDate = models.DateField(blank=True, null=True)
    ClientContact = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.id} {self.FirstName} {self.LastName}"
    