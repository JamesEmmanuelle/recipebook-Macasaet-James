from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 50)

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(Auto_now_Add=True)