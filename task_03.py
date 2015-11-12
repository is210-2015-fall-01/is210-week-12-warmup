#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Warmup Task 03."""


import time


class CustomLogger(object):
    """CustomerLogger object."""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Log function."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Flush function."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Cannot Open Log File')
            raise IOError

        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('Cannot Write Log File')

        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
