#1
# my_fav_numbers={13,23}
# my_fav_numbers.add(7)
# my_fav_numbers.add(1)
# my_fav_numbers.pop()
# print(my_fav_numbers)
# friend_fav_numbers={15,2,0,9}
# our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#2
#No

#3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#4
# list1=[]
# num=1
# for i in range(1,6):
#     num+=0.5
#     list1.append(i)
#     list1.append(num)
# print(list1)

#5
# numbers=[]
# for i in range (1,21):
#     numbers.append(i)
# print(numbers)

#6
# name = str(input("Enter your name:"))
# while name != 'Zhenia':
#     name = input("Enter your name:")
# print("You did it!")

#7
# user_fruits=str(input("What is your favorite fruits?"))
# fruits=user_fruits.split(' ')
# fav_fruit=str(input("Enter one favorite fruit:"))
# if fav_fruit in fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#8
users_top = input(' enter a pizza toppings ')
print(f' you added {users_top} topping to their pizza.')
price = 12.5
all_toppings = []
all_toppings.append(users_top)
while users_top != 'quit':
    users_top = input(' enter a pizza toppings ')
    print(f' you added {users_top} topping to their pizza.')
    price += 2.5
    all_toppings.append(users_top)
    if users_top == 'quit':
        price += 2.5
        print(f'price is: {price}')
        print(f'the list of your toppings is: {all_toppings}')
        break

    