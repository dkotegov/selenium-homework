# -*- coding: utf-8 -*-
import seismograph

from tests import (
    channels_test,
    videopreview_test,
    comments_test
)
suites = [
    channels_test.suite,
    videopreview_test.suite,
    comments_test.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)
