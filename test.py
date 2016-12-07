# -*- coding: utf-8 -*-
import seismograph

from tests import five_plus
from tests import no_ad
from tests import test_auth

suites = [
    #five_plus.suite,
    #no_ad.suite,
    test_auth.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
