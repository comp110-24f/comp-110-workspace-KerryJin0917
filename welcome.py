"""A welcoming test program to start COMP110"""

__author__ = "01234567"

print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3 the COMP110 Team!")

print("U" + "N" + "C")


def i_ate(num: int) -> None:
    "Tell us how you eat"
    if num < 29:
        print("ima bus so hard")
    else:
        print("ayo wtf")
    print("its over for me")


i_ate(num=9)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] is letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("yo", "y"))

"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("HUGEEEEEEE")
