#1
# class Cat:
#     def __init__(self, cat_name: str, cat_age: int):
#         self.name = cat_name
#         self.age = cat_age

# cat1=Cat("Snowi",4)
# cat2=Cat("Flafy",2)
# cat3=Cat("Max",12)

# def bigger():
#     if cat1.age > cat2.age and cat1.age > cat3.age:
#         print(f"The oldest cat is {cat1.name}, and is {cat1.age} years old.")
#     elif cat2.age > cat1.age and cat2.age > cat3.age:
#         print(f"The oldest cat is {cat2.name}, and is {cat2.age} years old.")
#     else:
#         print(f"The oldest cat is {cat3.name}, and is {cat3.age} years old.")
 
# bigger()

#OR

# def oldest_cat(*cats):
#     oldest_cat = cats[0]
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat

#     print(f"Oldest cat: {oldest_cat.name}")

# oldest_cat(cat1, cat2, cat3)

#2
# class Dog:
#     def __init__(self,name: str,height: int):
#         self.name=name
#         self.height=height
    
#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         x=davids_dog.height*2
#         print(f"{self.name} jumps {x} cm high!")


# davids_dog=Dog("Rex",50)
# print(f"{davids_dog.name} is {davids_dog.height} size")
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog=Dog("Teacup",20)
# print(f"{sarahs_dog.name} is {sarahs_dog.height} size")
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger!")
# else:
#     print(f"{davids_dog.name} is bigger!")

#3
# class Song:
#     def __init__(self,lyrics: list):
#         self.lyrics=lyrics
#     def sing_me_a_song(self):
#         for word in self.lyrics:
#             print(word)

        
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()