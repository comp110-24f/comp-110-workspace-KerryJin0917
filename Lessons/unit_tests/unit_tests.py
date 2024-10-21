from Lessons.unit_tests.list_fns import get_first, get_and_remove_first, remove_first


def test_get_first() -> None:
    foods: list[str] = ["apples", "watermelon", "steak", "pasta", "Burger"]
    assert get_first(foods) == "apples"


def test_remove_first_ret_value() -> None:
    """Test that removes first returns None."""
    foods: list[str] = ["apples", "watermelon", "steak", "pasta", "Burger"]
    assert remove_first(foods) == None


def test_remove_first_behavior() -> None:
    """Test that remove first removes first element."""
    foods: list[str] = ["apples", "watermelon", "steak", "pasta", "Burger"]
    remove_first(foods)
    assert get_first([]) == ""
