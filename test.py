# -*- coding: utf-8 -*-
import seismograph

from tests import five_plus
from tests import smiles


suites = [
    five_plus.suite,
    smiles.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py',
                     suites=suites)
