#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Warmup Task 01."""


def simple_lookup(var1, var2):
    """Index Search.
    Attributes:
        var1(mixed): variable.
        var2(mixed): variable.
    Return:
        var1
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
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
