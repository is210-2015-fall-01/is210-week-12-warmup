#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This is a simple lookup module to demonstrate exception handling.

    Args:
        var1 (list): A list.
        var2 (int): An index of the list.

    Returns:
        var1[var2]: The element in index var2 of var1 list.

    Example:
        >>> simple_lookup([1,2], 1)
        2
"""
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
