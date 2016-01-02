#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module. For Invalid Age error"""


import datetime


class InvalidAgeError(Exception):
    """class IAE docstring."""
    pass


def get_age(birthyear):
    """Age calculated from birthyear.
    Args:
        birthyear(int): year born
    Returns:
        age(int) or InvalidAgeError, if not valid
    Examples:
    >>> get_age(2014)
    1
    >>> get_age(2016)

    Traceback (most recent call last):
      File "<pyshell#1>", line 1, in <module>
        get_age(2016)
      File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py",
          line 24, in get_age
        raise InvalidAgeError
    InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
