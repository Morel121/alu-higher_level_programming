#!/usr/bin/python3
"""
This module defines a class Rectangle with a class attribute
to define the print symbol.
"""


class Rectangle:
    """
    Defines a rectangle by width and height, tracking instances
    and allowing a custom print symbol.

    Attributes:
        number_of_instances (int): Total count of active instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle and increments instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # Convert symbol to string just in case it's a different type
        symbol = str(self.print_symbol)
        rows = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns string representation to recreate instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when deleted and decrements instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
