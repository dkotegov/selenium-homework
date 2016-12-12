# -*- coding: utf-8 -*-

import seismograph

from tests import my_holidays

test_suites = [
    my_holidays.suite,
]

if __name__ == '__main__':
    seismograph.main(config_path="conf.base_config", suites=test_suites)
