from django.db import models
from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.TextField(max_length=100)

class contact(models.Model):
    messageId = models.AutoField(auto_created=True,primary_key=True)
    name = models.TextField(max_length=100,null=True)
    phone =models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=50,null=True)
    message = models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return super().__str__()
        return self.name


class review(models.Model):
    image = models.ImageField(null = True)
    rate = models.FloatField(max_length=2 , null = True)
    price = models.FloatField(max_length=1000 , null = True)
    location = models.CharField(max_length = 100, null=True)
    Name = models.CharField(max_length = 100, null=True)
    Item = models.CharField(max_length = 100, null=True)
    description = models.CharField(max_length = 1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)