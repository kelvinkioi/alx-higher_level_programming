#!/usr/bin/python3
"""text func"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError('text must be a string')
    w = text
    i = 0
    while i < len(w):
        print(w[i], end='')
        if w[i] in ':?.' or w[i] == '\n':
            print(end='\n\n')
            i += 1
            while i < len(w) and (w[i] == ' ' or w[i] == '\t'):
                i += 1
            continue
        i += 1
