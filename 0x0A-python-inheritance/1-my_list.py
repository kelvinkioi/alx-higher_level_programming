#!/usr/bin/python3
"""defines inherited list class MyList."""


class MyList(list):
    """implements sorted print for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order, assumed to be
        of type int"""
        print(sorted(self))
