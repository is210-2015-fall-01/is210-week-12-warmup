#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger class"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A log function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function"""
        try:
            handled = []
            fhandler = open(self.logfilename, 'a')
        except IOError:
            raise IOError
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            raise IOError
        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            raise IOError
        finally:
            fhandler.close()
