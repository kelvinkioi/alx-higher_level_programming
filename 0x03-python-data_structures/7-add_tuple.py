#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_1 = list(tuple_a)
    if len(list_1) < 2:
        for i in range(len(list_1), 2):
            list_1.append(0)

    list_2 = list(tuple_b)
    if len(list_2) < 2:
        for i in range(len(list_2), 2):
            list_2.append(0)
    n = [list_1[0] + list_2[0], list_1[1] + list_2[1]]
    new_tuple = tuple(n)
    return new_tuple
