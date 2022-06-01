from django.db import models
from unicodedata import name
import datetime as dt

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to ='images/',null=True)
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField(max_length=40)



class Category(models.Model):
     categories =(
         ('Travel', 'Travel'),
         ('Food', 'Food'),
         ('Design', 'Design'),
     )
     name = models.CharField(max_length=50, choices=categories)




 