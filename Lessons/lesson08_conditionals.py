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
    print("ehhehehehe")


less_than_10(num=1)


def number_info(num: int) -> int:
    if num < 10:
        print("Small Number")
    else:
        if num % 2 == 0:
            print("EVEN")
        else:
            print("UR ODD")
    return num


number_info(num=11)

print(number_info(num=4))


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("why are u aguhgaughaugh")
    elif weather == "hot":
        print("ima buss")
    else:
        print("ayo wtf is this")
    return weather


get_weather_report()
