#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def simple_lookup(var1, var2):
    """No key access.
    Attributes:
        var1(mixed): an argument variable
        var2(mixed): an argument variable
    Returns:
        Will return an exception.
    Example:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1,2]
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key does not exist.'
        return var1
