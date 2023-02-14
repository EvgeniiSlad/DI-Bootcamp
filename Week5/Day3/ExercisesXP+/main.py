from datetime import datetime , timedelta
from datetime import date
from random import randint
import string
import random
from datetime import date

#2
def accepts_number(number:int) -> str:
    random_number = randint(0,101)
    if number == random_number:
        print('display a success message to the user')
accepts_number(1)

#3
random_string = ''.join(random.choices(string.ascii_letters, k = 5))
print(random_string)

#4
def cordate():
    now_date = date.today()
    print(now_date)
cordate()

#5
def until_january():
    today = datetime.now()
    january_1st = datetime(2024, 1 , 1, 00, 00)
    print(january_1st - today)
until_january()

#6
def minutes_you_lived(birthdate):
    today = datetime.now()
    difference = today - birthdate
    difference_in_sec = difference.total_seconds
    minutes = divmod(difference_in_sec(), 60)[0]
    return(f'minutes {minutes}')

print(minutes_you_lived(datetime(1999, 7 , 1, 00, 00, 00)))

#7


#8
class Age:
    def __init__(self, seconds:int) -> None:
        self.seconds = seconds
        self.one_year_on_earth = seconds/31557600

    def on_earth(self):
        return round(self.one_year_on_earth,2)
    def on_mercury(self):
        return round(self.one_year_on_earth / 0.2408467,2)
    def on_venus(self):
        return round(self.one_year_on_earth / 0.61519726,2)
    def on_mars(self):
        return round(self.one_year_on_earth / 1.8808158,2)
    def on_jupiter(self):
        return round(self.one_year_on_earth /  11.862615,2)
    def on_saturn(self):
        return round(self.one_year_on_earth /  29.447498,2)
    def on_uranus(self):
        return round(self.one_year_on_earth / 84.016846,2)
    def on_neptune(self):
        return round(self.one_year_on_earth / 164.79132,2)

iam = Age(1000000000)
print(iam.on_neptune())