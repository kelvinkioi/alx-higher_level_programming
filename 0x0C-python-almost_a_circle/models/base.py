#!/usr/bin/python3
"""My first class Base"""


class Base:
    """Defining a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialization
        Args:
            id: id is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)
