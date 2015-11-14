#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    "Logging class."

    def __init__(self, logfilename):
         """A constructor for class CustomLogger.

        Args:
            logfilename- name of log file.
            
       Attributes:
           msg(list) - An empty list
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A function with a list and a timestamp.

       Args:
           msg(list)- An empty list
           timestamp- defaults to None
           
       Attributes:
          timestamp and msg.
       """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        " Attributes- An empty list- handled"
        try:
            handled = []
            fhandler = open(self.logfilename, 'a')

        except IOError:
            self.log('Log file cannot open')
            raise IOError()

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            
        except IOError:
            self.log('File cannot be written to')

        for index in handled[::-1]:
            del self.msgs[index]

            fhandler.close()
