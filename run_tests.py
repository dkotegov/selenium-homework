# -*- coding: utf-8 -*-
# #!/usr/bin/env python2

import seismograph
from tests import test_creation_post
from tests import test_group_settings
from tests import test_group_navigation


suites = [
    # test_creation_post.suite,
    # test_group_settings.suite,
    test_group_navigation.suite,
]
if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)
