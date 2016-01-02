#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """This is a exception class"""
    pass


def get_age(birthyear):
    """A function to test the age.

    This is a small function to demonstrate the exception handling
    usage.

    Args:
        birthyear (int): The birth year (four digits)

    Returns:
        age (int): Age based on birth year

    Example:
        >>> get_age(2012)
        3
"""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    else:
        return age
