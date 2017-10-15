
__author__ = ["Arun Reghunathan"]

import logging

from project.worker import worker


logger = logging.getLogger('worker')

@worker.task()
def test():
    print "test task ... "

