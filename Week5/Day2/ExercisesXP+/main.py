#1
class Family:
    def __init__(self,members: list[dict],last_name: str):
        self.members=members
        self.last_name=last_name

    def born(self, **child):
        self.members.append(child)
        print('Congratulating the family!')
        print(self.members)
    
    def is_18(self, name):
        for member in self.members:
            for i in member:
                if member[i] == name:
                    if member['age'] >= 18:
                        return True
                    else:
                        print(member['age'])
                        return False

    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(member['name'])


# fam1=Family([
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ],'Sladkov')
# fam1.born(name ='Sasuke',age = 1,gender = 'Female',is_child = True)
# fam1.family_presentation()
# print(fam1.is_18('Michael'))

#2
class TheIncredibles(Family):
    def __init__(self, members, last_name) -> None:
        self.members = members
        self.last_name = last_name
    def use_power (self):
        for member in self.members:
                    if member['age'] >= 18:
                        print(member['name'] + ': ' + member['power'])
                    else:
                        raise ValueError('little kid')

    
    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(member['incredible_name'] + ': ' + member['power'])
    

fam2 = TheIncredibles([
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
], 'Sladkov')
fam2.use_power()
fam2.born(name ='Sasuke',age = 1,gender = 'Female',is_child = True, power = 'Unknown Power', incredible_name ='Baby Jack')
fam2.incredible_presentation()