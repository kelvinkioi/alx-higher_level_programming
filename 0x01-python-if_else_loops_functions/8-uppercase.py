#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            up = chr(ord(character) - 32)
            print("{}".format(up), end="")
        else:
            print("{}".format(character), end="")
    print()
