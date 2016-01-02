#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """A really good docstring

    Examples:
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
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
