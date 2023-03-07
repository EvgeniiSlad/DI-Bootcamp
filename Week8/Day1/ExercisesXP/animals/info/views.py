from django.shortcuts import render
import json
from .models import Family, Animal
from django.http import HttpResponse

# Create your views here.
with open('info/data.json', 'r') as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

def family(request, id):
    family_specific = Family.objects.get(id=id)
    family_animals = family_specific.animal_set.all()

    context = {'family': family_specific, 'animals': family_animals}

    return render(request, 'family.html', context)

def animal(request, id):
    animal_specific = Animal.objects.get(id=id)
    fam = animal_specific.family.name
    context = {'animal': animal_specific,'fam': fam}

    return render(request, 'animal.html', context)

def show_animals(request):
    # animals = Animal.objects.all()
    # return render(request, 'animals.html', {'animals':animals})
    animals = Animal.objects.all().order_by('family__name','name')
    count = Animal.objects.all().count()
    context = {'animals': animals,'count':count}
    return render(request, 'animals.html', context)


# Animal.objects.all().order_by('name')
# Animal.object.all().count()
