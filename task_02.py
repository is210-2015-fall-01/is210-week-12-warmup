#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    "raising an exception."
    pass


def get_age(birthyear):
    "Calculating age."
    age = datetime.datetime.now().year - birthyear
    if age <= 0:
        raise InvalidAgeError()

    return age
