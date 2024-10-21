"""Summing the elements of a list using different loops"""

__author__ = "730813572"


def w_sum(vals: list[float]) -> float:
    index = 0
    total = 0
    while index < len(vals):
        total = total + vals[index]
        index = index + 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0
    for elem in vals:
        total = total + elem
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0
    for idx in range(0, len(vals)):
        total = total + vals[idx]
    return total


print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.1, 0.9, 1.0]))
