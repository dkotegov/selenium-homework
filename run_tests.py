#!/usr/bin/env python2

import sys
# import seismograph
import unittest
from tests.test_creation_post import ExampleTest

# suite = ExampleTest(__name__)
if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ExampleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

    # seismograph.main()