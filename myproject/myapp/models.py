from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField("Phone number", max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    note = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    
class Product(models.Model):
    ProductID: models.ImageField()
    name: models.TextField()
    category: models.TextField()
    class Meta:
        permissions = [("can_change_category", "Can change category")]
