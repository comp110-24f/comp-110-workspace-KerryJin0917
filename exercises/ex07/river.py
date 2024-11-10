"""File to define River class."""

__author__ = "730813572"

from fish import Fish
from bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_b: list[Bear] = []
        new_f: list[Fish] = []
        for fish in self.fish:
            if fish.age < 3:
                new_f.append(Fish())
        for bear in self.bears:
            if bear.age < 5:
                new_b.append(Bear())
        self.fish = new_f
        self.bears = new_b
        return None

    def remove_fish(self, amount: int):
        for index in range(0, len(self.fish)):
            if index < amount:
                self.fish.pop(0)

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None

    def check_hunger(self):
        alive_b: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                alive_b.append(bear)
        self.bears = alive_b
        return None

    def repopulate_fish(self):
        baby_f: float = (len(self.fish) // 2) * 4
        for _ in range(baby_f):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        baby_b: float = len(self.bears) // 2

        for _ in range(baby_b):
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        index = 0
        while index < 7:
            self.one_river_day()
            index += 1
        return None
