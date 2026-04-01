#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): Private instance attribute representing square size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the new square.
        """
        self.__size = size
