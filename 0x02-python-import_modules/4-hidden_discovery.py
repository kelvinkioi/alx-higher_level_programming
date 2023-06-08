#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for j in name:
        if j[:2] != "__":
            print(j)
