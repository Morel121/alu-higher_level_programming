#!/usr/bin/python3
"""
This module defines a class Square with a private attribute size,
accessors, validation, area calculation, and a print method.
"""


class Square:
    """
    Defines a square with private size, property decorators, area,
    and a method to print the square using '#'.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        self.size = size

    @property
    def size(self):
        """Getter to retrieve the private __size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the private __size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
