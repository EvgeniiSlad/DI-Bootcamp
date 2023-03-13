from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def customers(requset):
    customers_list = Customer.objects.all().order_by('first_name','last_name')
    context = {'customers': customers_list}

    return render(requset,'customers.html',context)


def customer(requset,id:int):
    customers_odj = Customer.objects.get(id=id)
    context = {'customer': customers_odj}

    return render(requset,'customer.html',context)


def add_cust(request):

    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        form_filled.save()

    form = CustomerForm()
    context = {'form':form}

    return render(request,'add.html',context)


def rentals(request):
    rentals_list = Rental.objects.all()
    context = {'rentals': rentals_list}

    return render(request,'rentals.html',context)


def rental(request,id:int):
    rental = Rental.objects.get(id=id)
    context = {'rental': rental}

    return render(request,'rental.html',context)


def vehicles(request):
    vehicle_list = Vehicle.objects.all()
    context = {'vehicles':vehicle_list}

    return render(request,'vehicles.html',context)


def vehicle(request,id:int):
    vehicle = Vehicle.objects.get(id=id)
    context = {'vehicle':vehicle}

    return render(request,'vehicle.html',context)

def add_vehicle(request):

    if request.method == 'POST':
        form_filled = VehicleForm(request.POST)
        form_filled.save()

    form = VehicleForm()
    context = {'form':form}

    return render(request,'add1.html',context)
