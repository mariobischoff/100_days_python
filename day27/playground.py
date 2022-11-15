def add(*args):
    return sum(args)

add(2,3,4,5,6,7,8)


def calculate(**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.make)