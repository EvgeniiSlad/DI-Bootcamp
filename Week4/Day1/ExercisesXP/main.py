#EX1
text = str("Hello world\n")
print(text*4)

#EX2
num = (99 ** 3) * 8 
print(num)

#EX3
5 < 3 #True  
3 == 3 #True
# 3 == "3" #eror
# "3" > 3 #eror
"Hello" == "hello" #true

#EX4
computer_brand="MacBook"
print(f"I have a {computer_brand} computer")

#EX5
name="Zhenia"
age=23
shoe_size=43.5
info=f"I`am {name}, i {age} years old and my shoe size is {shoe_size}"
print(info)

#EX6
a:int = 6
b:int = 4
if a > b:
    print("Hello World") 

#EX7
num=int(input("Write a number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

#EX8
name = str(input("What is your name:"))
if name == "Zhenia":
    print(f"No {name}, it`s only my name!")

#EX9
height=int(input("What is your height in inches?"))
sms=height*2.54
if sms>145:
    print("You are tall enough for this")
else:
    print("You are not tall enough for this")