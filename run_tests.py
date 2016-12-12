# -*- coding: utf-8 -*-
import seismograph
from tests import lenta_tests
from tests import auth_tests
from tests import post_tests
from tests import lenta_tests
from tests import reshari_tests

suites = [
    post_tests.suite,
    lenta_tests.suite,
    reshari_tests.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
