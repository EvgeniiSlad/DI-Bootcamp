from django.db import models
from country_list import countries_for_language
# Create your models here.
countries = countries_for_language('en')
categories_list = [("action","action"), ("adventure","adventure"), ("comedy","comedy"), ("drama","drama"), ("fantasy","fantasy"), ("horror","horror"), ("musicals","musicals"), ("mystery","mystery"), ("romance","romance"), ("science-fiction","science-fiction"),  ("sports","sports"), ("thriller","thriller"), ("Western","Western")]



class Country(models.Model):
    name = models.CharField(max_length=30,choices=countries)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=30,choices=categories_list)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()



class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)

    created_in_country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='films_created')
    available_in_countries = models.ManyToManyField(Country, related_name='films_available')
    category = models.ManyToManyField(Category,related_name='films')
    director = models.ManyToManyField(Director,related_name='films')

    def __str__(self):
        return self.title

