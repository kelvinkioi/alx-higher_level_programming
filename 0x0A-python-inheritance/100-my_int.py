#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """ my int classthhat takes an args int"""

    def __eq__(self, value):
        """changes == opeartor to != """
        return self.real != value

    def __ne__(self, value):
        """changes != operator to == """
        return self.real == value
