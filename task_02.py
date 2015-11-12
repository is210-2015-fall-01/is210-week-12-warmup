#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Warmup Task 02."""


import datetime


class InvalidAgeError(Exception):
    """Age Checking Exception."""
    pass


def get_age(birthyear):
    """Checks the age entered.
    Args:
        birthyear(int): Age entered.

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
