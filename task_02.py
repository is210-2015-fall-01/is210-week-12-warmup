#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """An object that contains InvalidAgeError data.

    Args:
        It has one argument, Exception.
    """
    pass

def get_age(birthyear):
    """A function that contains get_age data.

    Args:
        It ahs one argument, birthyear.
        
    Returns:
        An integer.
        
    Examples:
        >>> get_age(1876)
        age 139
    """ 
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError(age)
    return age
