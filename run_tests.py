#!/usr/bin/env python2

import sys
# import seismograph
import unittest
from tests.test_creation_post import CreationPostTest

# suite = ExampleTest(__name__)
if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreationPostTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

    # seismograph.main()