#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """This is a CustomLogger class"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A log function.

        This function appends a timestamp and message string
        to the msg list.

        Args:
            msg (str): A message string.
            timestamp (time, default=None): The time stamp.
        Returns:
            None
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function.

        This function writes the contents of the msg list into
        a log file.

        Args:
            None
        Returns:
            None
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Log file cannot be opened.')
            raise IOError()
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except IOError:
                    self.log('Cannot write to file.')
                    continue
            for index in handled[::-1]:
                del self.msgs[index]
            fhandler.close()
