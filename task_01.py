#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This function attempts to access any index or key.

    Args:
        var1(mix): any value.
        var2(mix): any value.

    Return:
        Return index or key.

    Examples:
        >>> simple_lookup([1, 2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
         }
    """
    try:
        return var1[var2]
    except IndexError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
    except KeyError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
