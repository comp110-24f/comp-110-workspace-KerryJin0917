"""EX05 Utility Tests"""

__author__ = "730813572"


def only_evens(input: list[int]) -> list:
    index = 0
    new: list[int] = []  # Create a list
    while index < len(input):
        if input[index] % 2 == 0:
            new.append(input[index])
        index = index + 1
    return new  # Return the list of even numbers


def sub(input: list[int], start: int, end: int) -> list:
    new: list[int] = []  # Create a list
    if len(input) == 0:  # Edge Cases
        return []
    if start >= len(input):
        return []
    if start < 0:
        start = 0
    if end <= 0:
        return []
    if end < len(input):
        end = len(input) - 1
    while start < len(input):
        new.append(input[start])
        start = start + 1
        if start == end:
            return new
    return new  # Return the list of even numbers


def add_at_index(input: list[int], element: int, list_index: int) -> None:
    if list_index < 0:
        raise IndexError("Index is out of bounds for the input list")
    if list_index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(element)  # Add int to end of list

    index: int = len(input) - 2
    while index >= list_index:  # Shift index to correct spot
        sub_int: int = input[index + 1]
        input[index + 1] = input[index]
        input[index] = sub_int
        index = index - 1
    print(input)
    return None


list_2 = [1]
list_1 = [1, 2, 3, 5, 6, 7, 8]
add_at_index(list_1, 4, 4)
