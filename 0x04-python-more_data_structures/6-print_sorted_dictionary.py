#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_key = a_dictionary.keys()
    my_key = sorted(key)
    for i in my_key:
        print("{}: {}".format(i, a_dictionary[i]))
