"""Plan a Tea Party"""

__author__ = "730813572"


def main_planner(guests: int) -> None:
    """The entrypoint of this program"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # Concatenate string with number of guests
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # More accurate would be str(tea_bags(people=guests))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # Cost has 2 parameters, have to define both for it to work
    # Called on the tea_bags function for tea_count argument
    # and treats function for treat_count argument
    return None


def tea_bags(people: int) -> int:
    """Number of teabags needed based on number of people"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed based on number of people"""
    return int(tea_bags(people=people) * 1.5)


# Call on tea_bags to get correct number of treats


def cost(tea_count: int, treat_count: int) -> float:
    """Cost needed for tea & treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
