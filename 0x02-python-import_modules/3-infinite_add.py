#!/usr/bin/python3
import sys

if __name__ == '__main__':
    av = sys.argv
    n = len(av)
    total = 0
    if n > 1:
        for i in range(1, n):
            total += int(av[i])
    print(total)

