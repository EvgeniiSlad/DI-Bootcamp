import random
#1
words=str(input("Write a string:"))
if len(words)<10:
    print("String not long enough")
elif len(words)>10:
    print("string too long")

#2
print(words[0])
print(words[-1])

#3
srtin=str(input("Your string:"))
letters:str=""
for x in srtin:
    letters+=x
    print(letters)


#4
words = list(words)
random.shuffle(words)
print(words)
