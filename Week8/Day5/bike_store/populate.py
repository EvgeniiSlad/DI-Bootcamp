import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Customer
from faker import Faker

fake = Faker(locale='en_US')
def crate_cust(number:int):

    for _ in range(number):

        customer = Customer(first_name=fake.first_name(), 
                    last_name=fake.last_name(), 
                    email=fake.email(), 
                    phone_number=fake.msisdn(), 
                    address=fake.address())
        customer.save()

crate_cust(100)