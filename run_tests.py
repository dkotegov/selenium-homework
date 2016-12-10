# -*- coding: utf-8 -*-
import seismograph

import videopreview_test
import channels
import tests.single_video as sv

suites = [
    sv.suite,
    channels.suite,
    videopreview_test.suite,

]

if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)