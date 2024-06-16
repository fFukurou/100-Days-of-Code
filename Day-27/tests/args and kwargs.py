
#*args --> Tuple
def add(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add(1,2,3,4,5,6,7,8,9,10))

#**kwargs --> Dictionary
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']

    return n

print(calculate(10, add=2, multiply=5))


class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')



my_car = Car(make="idk bruh", model="carsamiright", seats=7)

print(my_car.seats)