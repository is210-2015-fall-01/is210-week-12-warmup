#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """This class inform invaild error."""

    pass


def get_age(birthyear):
    """This funcation calls and return valid birth year.

    Args:
        birthyears(int): birth year.

    Returns:
        age(int): birth year.

    Examples:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
