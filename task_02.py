#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Class docstring"""
    pass


def get_age(birthyear):
    """Converts birth year to age.

    Args:
        birthyear (numeric): should be a 4-digit number

    Returns:
        age (numeric): equals current year minus birthyear

    Raises:
        InvalidAgeError: If age is less than zero.
    """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
