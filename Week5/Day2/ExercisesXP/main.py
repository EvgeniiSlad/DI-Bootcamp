#1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bengal_cat = Bengal('Snowi', 10)
# chartreux_cat = Chartreux('Max', 4)
# siamese_cat = Siamese('Loh', 1)
# all_cats = [bengal_cat, chartreux_cat, siamese_cat]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

#2
class Dog:
    def __init__(self,name: str,age: int,weight: int):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self)->str:
        return f'{self.name} is barking'
        
    def run_speed(self)-> int|float:
        rspeed: int=self.weight/self.age*10
        return rspeed

    def fight(self, other_dog):
        if other_dog.run_speed() * other_dog.weight > self.run_speed() * self.weight:
            print(f'{other_dog.name}')
        elif other_dog.run_speed() * other_dog.weight < self.run_speed() * self.weight:
            print(f'{self.name}')




if __name__=='__main__':
    dog_1 = Dog('Pusha', 10, 45)
    dog_2 = Dog('Joseph', 3, 15)
    dog_3 = Dog('Shar', 6, 60)
    dog_1.bark()
    print(dog_2.run_speed())
    dog_3.fight(dog_2)