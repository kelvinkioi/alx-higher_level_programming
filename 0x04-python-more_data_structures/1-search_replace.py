#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = my_list.copy()
    for n, i in enumerate(new_l):
        if i == search:
            new_l[n] = replace
    return new_l
