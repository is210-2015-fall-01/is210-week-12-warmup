#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger class."""

    def __init__(self, logfilename):
        """Docstring. Constructor. CustomLogger class.
        Attributes:
            None
        Args:
            longfilename(str)
            msgs(list)
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """log method docstring.
        Args:
            msg: from log
            timestamp: Unix
        Returns:
            A log of messages.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush function docstring."""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Logfile can not be opened.')
            raise IOError
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except IOError:
                    self.log('I/O error.Can not write to file.')

        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
