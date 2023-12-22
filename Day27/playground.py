def add(*args):
    total = 0
    for n in args:
        total += n

    print(total)


# add(5, 10, 15, 20)
#

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
