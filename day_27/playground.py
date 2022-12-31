def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 56, 7, 989, 9))


def calculate(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key)
        print(value)


print(calculate(add=3, multiply=4))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
