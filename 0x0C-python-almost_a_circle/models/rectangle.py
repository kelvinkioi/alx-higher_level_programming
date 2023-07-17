#!/usr/bin/python3
"""Defines a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class rectangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialization
        Args:
            width:
            height:
            x: 0 as default
            y: 0 as default
            id: Super class
        """
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """stter for height"""
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(' ', end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):

        """function that returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """args: assigns an argument to each attribute
        kwargs: assigns a key/value argument to attributes"""
        if len(args) == 0:
            for i in kwargs:
                if i == 'id':
                    self.id = kwargs[i]
                if i == 'width':
                    self.width = kwargs[i]
                if i == 'height':
                    self.height = kwargs[i]
                if i == 'x':
                    self.x = kwargs[i]
                if i == 'y':
                    self.y = kwargs[i]
            return
        for i in range(len(args)):
            if (i == 0):
                self.id = args[0]
            elif (i == 1):
                self.width = args[1]
            elif (i == 2):
                self.height = args[2]
            elif(i == 3):
                self.x = args[3]
            elif (i == 4):
                self.y = args[4]
            else:
                break
