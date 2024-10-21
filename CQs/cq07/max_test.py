"""testing functions for CQ07"""

__author__ = "730813572"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    a: list[int] = [1, 2, 3, 4]
    assert find_and_remove_max(a) == 4


def test_input() -> None:
    a: list[int] = [1, 2, 3, 4]
    find_and_remove_max(a)
    assert a == [1, 2, 3]


def test_empty_list() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
