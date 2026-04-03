#!/usr/bin/python3
"""
This module defines a Student class with a reload method.
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
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance with values 
        from the json_data dictionary.

        Args:
            json_data (dict): A dictionary where keys are attribute names.
        """
        for key, value in json_data.items():
            if key in self.__dict__:
                setattr(self, key, value)
