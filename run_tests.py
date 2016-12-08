# -*- coding: utf-8 -*-
import seismograph

import videopreview_test
import base_case

suites = [
    base_case.suite
    #videopreview_test.suite,
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
suites=suites)