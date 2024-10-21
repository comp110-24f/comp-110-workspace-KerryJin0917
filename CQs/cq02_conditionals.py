"""My second Challenge Question in COMP110"""

__author__ = "730813572"


def guess_a_number() -> None:
    secret: int = 7
    number = int(input("Guess a number: "))
    print("Your guess was " + str(number))
    if number == 7:
        print("You got it!")
    elif number < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


guess_a_number()

if __name__ == "__main__":
    guess_a_number()
