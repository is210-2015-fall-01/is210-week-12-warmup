#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Tries to index/key one argument to the other argument.

    Args:
        var1, var2: can be anything

    Returns:
        a list indexed/keyed by var2.

    Raises:
        If the index/key doesn't exist, prints an error message
        and returns var1.
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
