# -*- coding: utf-8 -*-

import sys, getopt
import unittest
from tests.group_messages_test import GroupMessagesTest
from tests.audio_messages_test import AudioMessagesTest
from tests.video_messages_test import VideoMessagesTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
         unittest.makeSuite(AudioMessagesTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())