# -*- coding: utf-8 -*-
import seismograph

from tests import test_auth
from tests import five_plus

suites = [
    #test_auth.suite,
    five_plus.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
