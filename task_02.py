#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import datetime


class InvalidAgeError(Exception):
    """To obtain a valid age."""
    pass


def get_age(birthyear):
    """An age exception.
    Args:
        birthyear(int): age of user
    Returns:
        Will return an invalid age error when age is not valid.
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
