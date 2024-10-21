"""Practice with scope"""


def remove_chars(msg: str, char: str):
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"  # global variable

print(remove_chars(word, "o"))
print(remove_chars(word, "y"))
# print(remove_chars("football", "o"))
