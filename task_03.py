#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger class"""

    def __init__(self, logfilename):
        """A function"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A log function."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function."""
        handled = []

        for index, entry in enumerate(self.msgs):
            try:
                fhandler = open(self.logfilename, 'a')
            except IOError:
                self.log(msg='IOError')
                raise IOError
            else:
                self.log(msg='other Error')
                break
            finally:
                fhandler.close()
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
                for index in handled[::-1]:
                    del self.msgs[index]
            except IOError:
                self.log(msg='IOError')
                break
            finally:
                fhandler.close()
