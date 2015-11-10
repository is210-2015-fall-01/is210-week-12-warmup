#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task03"""


import time


class CustomLogger(object):
    """A log class.
    Args:
        None
    Attribute:
        logfilename(str): a file name for loggers.
        msgs(list): a list of messages.
    """

    def __init__(self, logfilename):
        """A class instance.
        Attributes:
            None
        Args:
            logfilename(str): a file name for loggers.
            msgs(list): a list of messages.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Docstring.
        Args:
            msg(str): a message.
            timestamp(Unix Time Stamp): timestamp default to None.
        Returns:
            Logged messages and timestamps.
        Examples:
            >>> logger.log('hello')
            >>> logger.log('goodbye')
            logger.msgs
            [(1429838843.838129, 'hello'), (1429838858.844048, 'goodbye')]
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A simple login.
        Args:
            None
        Returns:
            None
        Examples:
            >>> open('somelongfilename')
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as error:
            self.log('Could not open file.')
            raise error

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            self.log('Another logging err.')

        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            self.log('Error Msg')
        except StandardError as error:
            self.log('Encountered some other error: {}'.format(error))
        finally:
            fhandler.close()
