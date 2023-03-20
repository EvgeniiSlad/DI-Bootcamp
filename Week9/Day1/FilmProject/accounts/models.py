from django.db import models
from django.contrib.auth.models import User
from films.models import *
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_films = models.ManyToManyField(Film)
    favorite_directors = models.ManyToManyField(Director)
    favorite_categories = models.ManyToManyField(Category)

    def __str__(self) :
        return f'User`s {self.user} profile'
    

