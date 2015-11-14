#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """An function that enables to look up for va1 and var2.

    Args:
        It has 2 arguments, var1 and var2.

    Returns:
        var1[var2] and then var1

    Examples:
        >>>simple_lookup([1,2], 4)
            Warning: Your index/key doesn't exist
            [1, 2]
        >>> simple_lookup({}, 'banana')
            Warning: Your index/key doesn't exist
    """
    try:
        var1[var2]
        return var1[var2]
    except (IndexError, KeyError):
        print 'Warning: Your index/key doesn\'t exist'
        return var1
    

