"Coordinates for cq04"

__author__ = "730813572"


def get_coords(xs: str, ys: str) -> None:
    index1 = 0
    while len(xs) > index1:
        index2 = 0
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 = index2 + 1
        index1 = index1 + 1


get_coords("123", "abc")
