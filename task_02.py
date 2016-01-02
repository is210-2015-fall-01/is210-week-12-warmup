#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """exception class."""
    pass


def get_age(birthyear):
    """A function that tests the age."""
    age = datetime.datetime.now().year - birthyear
    if not age > 0:
        raise InvalidAgeError()
    return age
