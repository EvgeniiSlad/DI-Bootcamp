import random
#1
# def display_message():
#     print("I lerning Python on this course")

# display_message()

#2
# def favorite_book(title:str):
#     print(f"One of my favorite books is {title} ")

# favorite_book('Harry Potter')

#3
# def describe_city(city:str,country:str):
#     print(f"{city} is in {country}")

# describe_city("Moscow","Russia")

#4




#5
# def make_shirt(size:str="large",text:str="I love Python"):
#     result=f"The size of the shirt is {size} and the text is {text}"
#     print(result)
# make_shirt()
# make_shirt('medium')
# make_shirt("small","loveee")

#6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians():
#     for name in magician_names:
#         print(name)
# show_magicians()
# def make_great ():
#     for name in magician_names:
#         print(f"The Great {name}")
# make_great()

#7
def get_random_temp (season = 'autumn'):
    if season == 'winter':
        random_degrees = random.randint(-10,6)
    if season == 'spring' or season == 'autumn'or season == 'fall':
        random_degrees = random.randint(7,25)
    if season == 'summer':
        random_degrees = random.randint(25,40)
    return random_degrees
# print(get_random_temp())

def season():
    users_month = int(input('enter a number of the month '))
    if 1 <= users_month <= 2 or users_month == 12:
        return 'winter'
    elif 3 <= users_month <= 5:
        return 'spring'
    elif 9 <= users_month <= 11:
        return 'autumn'
    elif 6 <= users_month <= 8:
        return 'summer'

def main():
    users_season = season()
    degrees = int(get_random_temp(users_season))
    print(f'The temperature right now is {degrees} degrees Celsius')
    if degrees < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= degrees <= 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 < degrees <= 24:
        print('nice weather')
    elif 24 < degrees <= 32:
        print('too hot')
    elif 32 < degrees <= 40:
        print('too hot, stau home')
    
main()
