#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """An object that stores CustomLogger data. """
    
    def __init__(self, logfilename):
        """A constructor for CustomLogger.

        Args:
            Has one argument, logfilename.

        Attributes:
            logfilename and an empty list called msgs.

        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A function with a list and a timestamp.

        Args:
            Has two arguments; msg and timestamp.

        Attributes:
            timestamp and a list.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A function called flush.

        Args:
            Has no arguments.

        Attributes:
            An emty list called handled.
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')

            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError as error_caught:
            self.log("Target log file cannot be opened")
            raise error_caught
        except:
            self.log("Other Error encountered")
        else:
            for index in handled[::-1]:
                del self.msgs[index]
        finally:
            fhandler.close()






