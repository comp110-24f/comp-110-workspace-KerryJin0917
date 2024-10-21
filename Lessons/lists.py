"""Basic syntax of list"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(5.0)
my_numbers.append(3.0)
print(my_numbers)

grocery_list: list[str] = ["bananas", "milk", "bread"]

grocery_list[0] = grocery_list[2]

grocery_list.pop(0)

print(grocery_list)


def display(Input: list[int]) -> None:
    index = 0
    while len(Input) > index:
        print(Input[index])
        index = index + 1


display(my_numbers)
