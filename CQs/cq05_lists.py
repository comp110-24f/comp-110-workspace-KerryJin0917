"""Mutating functions"""

__author__ = "730813572"


def manual_append(one: list[int], two: int) -> None:
    one.append(two)


def double(the_list: list[int]) -> None:
    index = 0
    while len(the_list) > index:
        the_list[index] = the_list[index] + the_list[index]
        index = index + 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
