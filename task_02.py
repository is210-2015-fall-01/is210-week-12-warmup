#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Class that raises an invalid age error."""
    pass


def get_age(birthyear):
    """Calculates age.

    Args:
        birthyear (int): year user was born.
    Returns:
        invalid age error IF year is not valid.
    Example:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
