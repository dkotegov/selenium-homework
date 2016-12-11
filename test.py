# -*- coding: utf-8 -*-
import seismograph

from tests import test_five_plus
from tests import test_smiles
from tests import test_invisible_mode
from tests import test_all_included
from tests import test_buy_oks

suites = [
    test_five_plus.suite,
    test_smiles.suite,
    test_invisible_mode.suite,
    test_all_included.suite,
    test_buy_oks.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)
