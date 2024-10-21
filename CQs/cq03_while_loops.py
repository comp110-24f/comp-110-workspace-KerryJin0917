"""My third Challenge Question in COMP110"""

__author__ = "730813572"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    show = 0
    while count < len(phrase):
        if phrase[count] == search_char:
            show = show + 1
        count = count + 1
    return show


print(num_instances("hello", "l"))
