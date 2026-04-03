#!/usr/bin/python3
"""
This module defines a Student class with filtered dictionary retrieval.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in 
        this list must be retrieved.

        Args:
            attrs (list): A list of strings representing attribute names.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__
