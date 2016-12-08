# -*- coding: utf-8 -*-
import seismograph

from tests import five_plus
from tests import smiles
from tests import test_invisible_mode
from tests import test_all_included

suites = [
    five_plus.suite,
    smiles.suite,
    test_invisible_mode.suite,
    test_all_included.suite,
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
