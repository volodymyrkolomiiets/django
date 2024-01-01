from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.DecimalField( 
                         max_digits = 5, 
                         decimal_places = 2) 
    
    class Meta:
        db_table = "person_info"
    
    
class Artist(models.Model):
    name = models.CharField(max_length=10)
    
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)