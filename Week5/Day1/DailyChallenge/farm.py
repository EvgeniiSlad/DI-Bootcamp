class Farm:
    def __init__(self,name: str):
        self.name = name
        self.animals = {}

        print(f'{self.name}\'s farm')
    
    def add_animal(self, animal, quantity = 1):
        if animal in self.animals.keys():
            quantity += 1
        self.animals[animal] = quantity
    
    def get_info(self):
        return self.animals

    def get_animal_types(self):
        key_list = list(self.animals.keys())
        return sorted(key_list)
        
    def get_short_info(self, *anymals):
        all = self.get_animal_types()
        return f"McDonalds farm has {', '.join(all)}"
        



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())