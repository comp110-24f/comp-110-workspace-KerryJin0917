"""EX05 Utility Tests"""

__author__ = "730813572"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index


def test_only_evens() -> None:
    """General use case test for only_evens, testing return"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    assert only_evens(list_1) == [2, 6, 8]


def test_sub() -> None:
    """General use case test for sub, testing return"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    assert sub(list_1, 1, 5) == [2, 3, 5, 6, 7]


def test_add_at_index() -> None:
    """General use case test for add_at_index, testing return"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    assert add_at_index(list_1, 4, 3) == None  # Make sure this returns None


def test_only_evens_mutate() -> None:
    """General use case test for only_evens, testing input mutation"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    only_evens(list_1)  # Returns [2, 6, 8]
    assert list_1 == [1, 2, 3, 5, 6, 7, 8]  # Make sure list is NOT mutated


def test_sub_mutate() -> None:
    """General use case test for sub, testing input mutation"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    sub(list_1, 1, 5)  # Returns [2, 3, 5, 6, 7]
    assert list_1 == [1, 2, 3, 5, 6, 7, 8]  # Make sure list is NOT mutated


def test_add_at_index_mutate() -> None:
    """General use case test for add_at_index, testing input mutation"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    add_at_index(list_1, 4, 3)  # Returns None, but should mutate list
    assert list_1 == [1, 2, 3, 4, 5, 6, 7, 8]  # Make sure list is mutated


def test_only_evens_edge() -> None:
    """General use case test for only_evens, testing edge case"""
    list_1 = [1, 3, 5, 7]
    assert only_evens(list_1) == []  # Edge case all odds, should return empty list


def test_sub_edge() -> None:
    """General use case test for sub, testing edge case"""
    list_1 = []
    assert (
        sub(list_1, 1, 5) == []
    )  # Edge case length of input == 0, should return empty list


def test_add_at_index_edge() -> None:
    """General use case test for add_at_index, testing edge case"""
    list_1 = [1, 2, 3, 5, 6, 7, 8]
    add_at_index(list_1, 9, 7)  # Edge Case, list_index at the very end
    assert list_1 == [1, 2, 3, 5, 6, 7, 8, 9]  # Make sure list is mutated correctly
