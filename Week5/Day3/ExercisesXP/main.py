#1
# def abs(value):
#     """The abs() function returns the absolute value of the given number."""

# def int():
#     """The int() function converts the specified value into an integer number."""

# def input():
#     """Python input() function is used to take user input"""

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)


#2
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self) -> str:
        fullstr=f'{self.amount} {self.currency}s'
        return fullstr
    
    def __int__(self) -> int:
        return self.amount
    
    def __repr__(self) -> str:
        rep=f'{str(self)}'
        return rep

    def __add__(self,value) ->int:
        if isinstance(value,int):
            return self.amount + value
        if isinstance(value,Currency):
            if self.currency == value.currency:
                return self.amount + value.amount
            else:
                raise TypeError('Cannot add between Currency type <dollar> and <shekel>')
    
    def __call__(self):
        # print(f'{self.amount} {self.currency}s')
        return f'{self.amount} {self.currency}s'
    
    def __iadd__(self,value):
        if isinstance(value,int):
            self.amount += value
            return self
        if isinstance(value,Currency):
             self.amount += value.amount
             return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1+c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1+c3)

