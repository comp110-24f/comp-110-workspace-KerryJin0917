def get_first(list_1: list[str]) -> str:
    """returns 1st element"""
    return list_1[0]


def remove_first(list_1: list[str]) -> list[str]:
    """removes first element then returns the remaining"""
    list_1.pop(0)
    return list_1


def get_and_remove_first(list_1: list[str]) -> str:
    """Remove and return 1st element"""
    first_ele: str = list_1[0]
    list_1.pop(0)
    return first_ele


print(get_and_remove_first(["help", "me"]))
