from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.TextField()