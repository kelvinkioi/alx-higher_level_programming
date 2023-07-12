#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if attrs is None:
            return self.__dict__
        a = {}
        for i in attrs:
            if i in self.__dict__:
                d[i] = self.__dict__[i]
        return a
