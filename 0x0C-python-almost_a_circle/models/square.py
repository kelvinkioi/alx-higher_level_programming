#!/usr/bin/python3
"""Defines a class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A Class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method returns [Square] (<id>) <x>/<y> - <size>"""
        id = self.id
        x = self.x
        y = self.y
        height = self.height
        return f"[Square] ({id}) {x}/{y} - {height}"
