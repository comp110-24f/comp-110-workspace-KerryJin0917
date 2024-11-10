"""EX06 Dictionary Utils: Functions that manipulate dictionaries"""

__author__ = "730813572"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function that inverts a dictionary by switching keys and values"""
    inverted_dict: dict[str, str] = {}
    for key in input:
        value = input[key]
        if value in inverted_dict:
            raise KeyError("There are two or more keys with the same name")
        inverted_dict[value] = key
    return inverted_dict


print(invert({"a": "z", "b": "y", "c": "x"}))


def favorite_color(input: dict[str, str]) -> str:
    """Function that returns string of favorite color"""
    color_count: dict[str, int] = {}
    for key in input:  # Loop through colors to count them
        color = input[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    fav: str = ""  # Create a string for favorite color
    max: int = 0  # Create a count
    for color in color_count:  # Change the color to be the favorite color
        if color_count[color] > max:
            max = color_count[color]
            fav = color
    return fav  # Return the color that appears most


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(input: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for elem in input:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


a = ["bruh", "bruh", "bruh"]
print(count(a))


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for word in input:
        if word != "":  # Check word is not empty
            letter = word[0].lower()  # Take the first letter and make it the key
            # lower function makes sure no new list is created for capital letter
            if letter not in result:
                result[letter] = (
                    []
                )  # Add letter as a key to the dictionary "result" and have empty list as value
            result[letter].append(word)  # Add the word to the values of the dictionary
    return result


print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    if day != "":  # Check to see day isn't an empty string
        if day not in input:  # If the day is not included in dictionary, add it as key
            input[day] = []  # Create an empty list for this new key
        if student not in input[day]:
            input[day].append(
                student
            )  # Mutate the dictionary by adding the student to the list/dict values


attendance_log: dict[str, list[str]] = {
    "Monday": ["Vrinda", "Kaleb"],
    "Tuesday": ["Alyssa"],
}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
