# -*- coding: utf-8 -*-

import sys
import unittest

from tests import PhotoLikeTestCase, VideoLikeTestCase, DiscussionLikeTestCase

if __name__ == '__main__':

    suite = unittest.TestSuite((
        unittest.makeSuite(PhotoLikeTestCase),
        unittest.makeSuite(VideoLikeTestCase),
        unittest.makeSuite(DiscussionLikeTestCase)
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
