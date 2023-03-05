from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.
with open('info/data.json', 'r') as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

def show_family(request,id):
    family_selected = None
    for family in families:
        if family['id'] == id:
            family_selected = family
    return render(request, 'family.html', family_selected)

def show_animal(request,id):
    animal_selected = None
    for animal in animals:
        if animal['id'] == id:
            animal_selected = animal
    return render(request, 'animal.html', animal_selected)

def show_animals(request):

    return render(request, 'animals.html', {'animals': animals})


def all_family(request):
    fam1 = []
    for animal1 in animals:
        if animal1['id'] == id:
            fam1.append(animal1['name'])

    return render(request, 'all_family.html', fam1)
