"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730813572"


def main() -> None:
    fiveletterword = input_word()
    oneletter = input_letter()
    contains_char(fiveletterword, oneletter)


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if (
        len(word) == 5
    ):  # length of word should be equivalent to 5 because want 5 character word
        print(word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) == 1:  # length of character equal to 1
        print(letter)
    else:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(the_word: str, the_letter: str) -> None:
    index = 0
    count = 0
    print("Searching for " + str(the_letter) + " in " + str(the_word))
    while index < len(the_word):
        if the_word[index] == the_letter:
            print(str(the_letter) + " found at index " + str(index))
            count = count + 1
        index = index + 1
        # While loop to search for the letters, index start at zero
        # Then index less than length of word so each character is
        # searched using the If statement

    if count == 0:
        print("No instances of " + str(the_letter) + " found in " + str(the_word))
    elif count == 1:
        print("1 instance of " + str(the_letter) + " found in " + str(the_word))
    else:
        print(
            str(count)
            + " instances of "
            + str(the_letter)
            + " found in "
            + str(the_word)
        )
        # Convert fucntions and variables to strings
        # in order to concacenate correctly


if __name__ == "__main__":
    main()
