"""Find max for CQ07"""

__author__ = "730813572"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index = 0
    big = input[0]  # Create an int
    while index < len(input):
        if input[index] > big:
            big = input[index]  # Change the int to be the biggest int
        index = index + 1
    count = 0
    while count < len(input):
        if input[count] == big:
            input.pop(count)
        else:
            count = count + 1
    print(input)
    return big  # Return the biggest int


a: list[int] = [1, 2, 3, 4]

print(find_and_remove_max(a))
