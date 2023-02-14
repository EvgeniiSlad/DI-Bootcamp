import random
from main import Dog

class PetDog(Dog):
    def __init__(self, name: str, age: int, weight: int) :
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play (self, *dogs: tuple):
        other_dogs_n=[dog.name for dog in dogs]
        other_dogs_nstr=", ".join(other_dogs_n)
        print(f'{self.name} and {other_dogs_nstr} all play togethe ')

    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll",
        f"{self.name} stands on his back legs",
        f"{self.name} shakes your hand",
        f"{self.name} plays dead"]
        if self.trained:
            print(random.choice(tricks))
        else:
            print(f'{self.name} is not trained!')



dog_1 = PetDog('Pusha', 10, 45)
dog_2 = PetDog('Joseph', 3, 15)
dog_3 = PetDog('Shar', 6, 60)
dog_1.play(dog_2,dog_3)
dog_1.train()
dog_1.do_a_trick()