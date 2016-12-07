# -*- coding: utf-8 -*-

import sys, getopt
import unittest
from tests.group_messages_test import GroupMessagesTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
         unittest.makeSuite(GroupMessagesTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())