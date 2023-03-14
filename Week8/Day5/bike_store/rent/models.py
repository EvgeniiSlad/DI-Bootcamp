from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200,blank=True,null=True)
    country  = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Vehicle(models.Model):
    type = models.ForeignKey('VehicleType', on_delete=models.CASCADE )
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey('rent.VehicleSize', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type},{self.size}'


class VehicleType(models.Model):
    vehicle_types = [
        ('C', 'City'),
        ('M', 'Mountain'),
        ('El', 'Electric'),
    ]
    name = models.CharField(max_length=2, choices=vehicle_types)

    def __str__(self):
        return self.name

class VehicleSize(models.Model):

    vehicle_sizes = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]
    name = models.CharField(max_length=2, choices=vehicle_sizes)

    def __str__(self):
        return self.name


class Rental(models.Model):

    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RentalRate(models.Model):

    daily_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)