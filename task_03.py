#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Class docstring"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Logs errors that occur in method execution."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """seeks out errors."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Unable to open file.')
            raise IOError
        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('I/O failure')
                continue
            except not IOError:
                self.log("Not an IO Error.")

        for index in handled[::-1]:
            try:
                del self.msgs[index]
            except IOError:
                self.log('Unable to write to disk')
                continue
            finally:
                fhandler.close()
