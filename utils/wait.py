#!/usr/bin/env python
# encoding: utf-8
import time
import datetime


WAIT_INTERVAL = 1

def calculate_time_duration(start):
    """
    Calculation duration
    """
    stop = datetime.datetime.now()
    seconds = int((stop - start).total_seconds())
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s

class RegressionException(Exception):
    """Regression test level exception base class"""

    def __init__(self, msg='', logger=None):
        # Exception information to be printed
        self.message = msg

        # If logger is configured, call logger.error to output an exception
        if logger:
            logger.error(msg)

        Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__

class TimeoutException(RegressionException):
    pass


class Wait:
    """
    Polling wait
    """

    def __init__(self, timeout, wait_interval=None):
        """
        :param timeout: Wait timeout
        :param wait_interval: Polling wait interval
        """
        self.timeout = timeout
        self.wait_interval = wait_interval if wait_interval else WAIT_INTERVAL
        self.start_time = time.time()

    def until(self, method, message=''):
        """
        Call the waiting step circularly, and judge whether to continue the waiting based on the result returned by the step
        If the wait has timed out, terminate the wait and throw an exception
        For waiting steps that do not do exception capture processing, please configure exception capture logic in step
        """
        end_time = time.time() + self.timeout
        while True:
            value = method()
            if value:
                return value
            time.sleep(self.wait_interval)
            if time.time() > end_time:
                break
        raise TimeoutException(message)
