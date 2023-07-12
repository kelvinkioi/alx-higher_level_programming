#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is not None:
            n_dict = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            for i in attrs:
                if i in self.__dict__:
                    n_dict[i] = self.__dict__[i]
            return n_dict
        else:
            return self.__dict__
