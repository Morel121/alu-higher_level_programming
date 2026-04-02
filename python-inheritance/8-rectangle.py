#!/usr/bin/python3
"""
Module for Rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intializes width and height after validation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
