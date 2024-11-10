"""OOP"""

__author__ = "730813572"


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx


p0: Point = Point(10.0, 0.0)

p0.translate_x(-5.0)

print(p0.dist_from_origin())
