from django.urls import path
from .views import show_animals, animal,family

urlpatterns = [
    path('family/<int:id>', family, name="family"),
    path('animal/<int:id>', animal, name="animal"),
    path('animals/',show_animals,name='animals_all'),
]