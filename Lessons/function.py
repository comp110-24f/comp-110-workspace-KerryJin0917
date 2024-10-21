"""Practice with Functions"""

from random import randint

random = randint(1, 9384)

print(random)


# Define a Function
def bigboi(food: int, drink: int) -> int:
    """Eat a meal"""
    return food + drink


# Call a Function
bigboi(food=1, drink=10)  # <- 1 and 10 are arguments

print(bigboi(291, 304))
