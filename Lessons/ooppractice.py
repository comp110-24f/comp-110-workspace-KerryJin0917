import math


class Circle:

    radius: float

    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return (self.radius**2) * math.pi


class Rectangle:
    height: float
    width: float

    def __init__(self, width: float, height: float):
        self.height = height
        self.width = width

    def area(self) -> float:
        return self.height * self.width


circ: Circle = Circle(2.0)
print(circ)
print(circ.area())

rect: Rectangle = Rectangle(4.0, 5.5)
print(rect)
print(rect.area())
