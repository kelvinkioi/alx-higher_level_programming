#!/usr/bin/python3
"""My first class Base"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([i.to_dictionary()
                        for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
