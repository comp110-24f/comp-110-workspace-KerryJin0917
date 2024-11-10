"""File to define Bear class."""


class Bear:

    age: int

    hunger_score: int

    def __init__(self):
        """constructor to initialize instances"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """simulate one day"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """eat"""
        self.hunger_score += num_fish
        return None
