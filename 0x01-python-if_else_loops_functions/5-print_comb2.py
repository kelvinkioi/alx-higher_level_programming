#!/usr/bin/python3
for i in range(100):
    if i <= 9:
        print("0{}, ".format(i), end="")
    elif i < 99:
        print("{}, ".format(i), end="")
    else:
        print("{}".format(i))
