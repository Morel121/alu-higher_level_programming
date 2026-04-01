#!/usr/bin/python3
"""
This module defines a class Square with size validation
and an area calculation method.
"""


class Square:
    """
    Defines a square by its size and provides area calculation.

    Attributes:
        __size (int): Private instance attribute representing square size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
