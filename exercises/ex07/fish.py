"""File to define Fish class."""


class Fish:

    age: int

    def __init__(self):
        """fish age"""
        self.age = 0
        return None

    def one_day(self):
        """get 1 day older"""
        self.age += 1
        return None
