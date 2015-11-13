#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Very simple logging class."""

    def __init__(self, logfilename):
        """Constructor.

            Attributes:
                    None
            Args:
                logfilename(str): logger name.
                msgs(list): a list of messages.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Log docstring.

        Args:
            msg: log message.
            timestamp: Unix timestamp.  Default set to None.
        Returns:
            A log for messages with a timestamp.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Flush docstring."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Could not open file')
            raise IOError

        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('Cannot write log file')

        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
