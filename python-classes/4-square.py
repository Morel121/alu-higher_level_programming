#!/usr/bin/python3
"""
This module defines a class Square with a private attribute size,
accessors (getter/setter), validation, and area calculation.
"""


class Square:
    """
    Defines a square with private size, property decorators, and area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        Uses the setter logic automatically by calling self.size = size.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter to retrieve the private __size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter to set the private __size attribute with validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.
        """
        return self.__size ** 2
