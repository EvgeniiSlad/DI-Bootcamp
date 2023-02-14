import math
class Circle:
    def __init__(self,radius: int) -> None:
        self.radius=radius
        self.diameter=radius*2

    def area(self):
        carea=math.pi*self.radius**2
        return carea

    def __str__(self):
        return f'radius: {self.radius} and diameter: {self.diameter}'

    def __add__(self,other):
        return self.radius + other.radius

    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __repr__(self):
        return str(self.radius)


c1 = Circle(2)
c2 = Circle(3)
print(f'r-{c1.radius} d-{c1.diameter}')
print(f'r-{c2.radius} d-{c2.diameter}')
print(c1.area())
print(c2.area())
print(c1+c2)
print(c1>c2)
print(c2>c1)
list=[c2,c1]
print(list)
list_sor=sorted(list)
print(list_sor)