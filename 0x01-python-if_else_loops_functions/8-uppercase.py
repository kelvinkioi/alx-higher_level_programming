#!/usr/bin/python3
def uppercase(str):
    result = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            up = chr(ord(character) - 32)
            result += "{}".format(up)
        else:
            result += "{}".format(character)
    print("{}".format(result))
