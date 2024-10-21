"""EX04 - Utils"""

__author__ = "730813572"


def all(match: list[int], number: int) -> bool:
    """Check to see if list matches the number"""
    if len(match) == 0:
        return False
    index = 0
    while index < len(match):
        if match[index] == number:
            # Check if each of the numbers match
            index = index + 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Find the maximum integer in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 0
    big = input[0]  # Create an int
    while index < len(input):
        if input[index] > big:
            big = input[index]  # Change the int to be the biggest int
        index = index + 1
    return big  # Return the biggest int


def is_equal(one: list[int], two: list[int]) -> bool:
    """Check if two lists are equal"""
    if len(one) == 0:
        if len(two) == 0:
            return True
        return False  # Edge case for if both are empty lists
    if len(two) == 0:
        if len(one) == 0:
            return True
        return False  # Same edge case, just other way around
    if len(one) != len(two):
        return False

    index = 0
    while index < len(one):
        if one[index] == two[index]:
            index = index + 1  # Check for equality
        else:
            return False
    while index < len(two):
        if one[index] == two[index]:
            index = index + 1  # Same check for equality
        else:
            return False
    return True


def extend(one: list[int], two: list[int]) -> None:
    """Append a list to another"""
    index = 0
    while index < len(two):
        one.append(two[index])  # Append the second list to the first
        index = index + 1
