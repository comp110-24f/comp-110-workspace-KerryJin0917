"""EX03 - Wordle"""

__author__ = "730813572"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1  # turn starts at 1, because first turn
    while turn <= 6:
        # give player 6 turns/guesses
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        # asks user for their guess
        print(emojified(secret, guess))
        # prints out the color-coded blocks that shows
        # whether the letter is correct, in the word, or incorrect
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    word = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(word) != secret_word_len
    ):  # length of word should be equivalent to length of secret word
        print(f"That wasn't {str(secret_word_len)} chars! Try Again: ")

    if len(word) == secret_word_len:
        print(word)
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check to see if the guessed character is in the secret word"""
    assert len(char_guess) == 1
    index = 0
    in_word: bool = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            in_word = True
            # Checks to see if the guess word character
            # matches with the secret word character depending on index
        index = index + 1
    return in_word
    # While loop to search for the letters, index start at zero
    # Then index less than length of word so each character is
    # searched using the If statement


def emojified(secret: str, guess: str) -> str:
    """Show what characters are in the correct position,
    or in the word but wrong position, or not in the word at all"""
    assert len(secret) == len(guess)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""
    # result is the variable that has the color blocks
    while index < len(secret):
        if secret[index] == guess[index]:
            result = result + GREEN_BOX
            # add color block to result depending on guess
        elif contains_char(secret, guess[index]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        index = index + 1
    return result


if __name__ == "__main__":
    main(secret="codes")
