#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """This class represents a very simple logging class.

    Attributes:
       None>
    """

    def __init__(self, logfilename):
        """This is simple function."""

        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """This function will check login.

         Args:
            msg(str): login message.
            timestamp(mix): Unix timestamp.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """This function validates logs.

        Args:
            None.

        Returns:
            None.
        """

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
