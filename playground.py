
# *args: Many Positional Arguments
"""
For example, made the function accept unlimited
numbers and then add them together
"""
def add(*args):
    print(args[0])
    print(type(args))

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6))

# ** kwards: Many Keyworded Arguments

def calculate(n, **kwargs):
    print(kwargs)  # It shows this is a dictionary format
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["add"])
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model =kw.get("model")  # The get if this model does not exist, then it would just return none
        self.colour = kw.get("colour")
        self.seats = kw.get("seat")

my_car = Car(make="Nissan", model="GTR")
print(my_car)
print(my_car.model)