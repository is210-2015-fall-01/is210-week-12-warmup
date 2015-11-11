#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Docstring. Constructor. CustomLogger."""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """log method docstring."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush method docstring."""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as error:  # check if called IOError
            self.log('Can not open file.')  # check if error message
            raise error

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError as error:  # check2 if called IOError
            self.log('Can not open file.')
            raise error  # maybe repeat

        finally:
            fhandler.close()

        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:  # check3
            self.log('Error. Does not remove stored messages.')
            raise error  # maybe repeat
        except StandardError as error:  # check4
            self.log('Another error: {}'.format(error))
