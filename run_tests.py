# -*- coding: utf-8 -*-
import seismograph

from tests import test_photo
suites = [
    test_photo.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
