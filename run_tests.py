# -*- coding: utf-8 -*-

import sys, getopt
import unittest
import tests.settings
from tests.group_messages_test import GroupMessagesTest
from tests.audio_messages_test import AudioMessagesTest
from tests.video_messages_test import VideoMessagesTest
from tests.simple_messages_test import SimpleMessagesTest


if __name__ == '__main__':
    tests.settings.Settings.get_login() and tests.settings.Settings.get_password()
    suite = unittest.TestSuite((
        unittest.makeSuite(AudioMessagesTest),
        unittest.makeSuite(SimpleMessagesTest),
        unittest.makeSuite(GroupMessagesTest),
        unittest.makeSuite(VideoMessagesTest)

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())