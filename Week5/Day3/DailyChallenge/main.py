import math
class Circle:
    def __init__(self,radius: int) -> None:
        self.radius=radius
        self.diameter=radius*2

    @classmethod
    def from_diameter(cls,diameter: int):
        return Circle(diameter//2)

    def area(self):
        carea=math.pi*self.radius**2
        return carea

    def __str__(self):
        return f'radius: {self.radius} and diameter: {self.diameter} area: {self.area():.2f}'

    def __add__(self,other):
        result=Circle(self.radius+other.radius)
        return result

    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __repr__(self):
        return str(self.radius)


c1 = Circle(2)
c2 = Circle.from_diameter(6)
print(c1)
print(c2)
c3=c1+c2
print(c3)
print(c1>c2)
print(c2>c1)
print(c1==c2)
list=[c2,c1,c3]
print(list)
list_sor=sorted(list)
print(list_sor)