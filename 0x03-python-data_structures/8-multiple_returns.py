#!/usr/bin/python3
def multiple_returns(sentence):
    k = len(sentence)
    if k != 0:
        c = sentence[0]
        return k, c
    return k, None
