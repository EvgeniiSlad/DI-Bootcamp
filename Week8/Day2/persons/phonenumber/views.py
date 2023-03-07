from django.shortcuts import render
from .models import Person
# Create your views here.


def numder(requests,number):
    person = Person.objects.get(phone_number = number)
    context = {'person': person}

    return render(requests,'main.html',context)

def name(request, name):
    person = Person.objects.get(name = name)
    context ={'person':person}

    return render(request,'name.html',context)