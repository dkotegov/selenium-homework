#!/usr/bin/env python2

import sys
# import seismograph
import unittest
from tests.test_creation_post import CreationPostTest
from tests.test_group_navigation import NavigationGroupTest
from tests.test_group_settings import GroupsSettingsTest

# suite = ExampleTest(__name__)
if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreationPostTest),
        unittest.makeSuite(NavigationGroupTest),
        unittest.makeSuite(GroupsSettingsTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

    # seismograph.main()
