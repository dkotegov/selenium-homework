# -*- coding: utf-8 -*-
import seismograph
from seismograph.ext import selenium

from tests import test_auth

suites = [
    test_auth.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
