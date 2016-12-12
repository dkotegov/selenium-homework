# -*- coding: utf-8 -*-

import sys, getopt
import unittest
from tests.group_messages_test import GroupMessagesTest
from tests.audio_messages_test import AudioMessagesTest
from tests.video_messages_test import VideoMessagesTest
from tests.simple_messages_test import SimpleMessagesTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
         unittest.makeSuite(AudioMessagesTest),unittest.makeSuite(SimpleMessagesTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())