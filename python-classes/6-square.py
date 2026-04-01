#!/usr/bin/python3
"""
This module defines a class Square with size and position attributes,
validation, area calculation, and a coordinate-aware print method.
"""


class Square:
    """
    Defines a square with private size and position, property decorators,
    area calculation, and a method to print using '#' at specific coordinates.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for private __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for private __size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for private __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for private __position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' at the coordinates defined by position.
        """
        if self.__size == 0:
            print("")
            return

        # Print the vertical offset (new lines)
        [print("") for i in range(self.__position[1])]

        # Print the square with horizontal offset (spaces)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
