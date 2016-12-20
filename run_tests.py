# -*- coding: utf-8 -*-

import seismograph

from tests import test_gifts_sections_list
from tests import test_gifts_tooltip
from tests import test_music_gifts
from tests import test_progressive_scroll
from tests import test_search_gifts

suites = [
    test_search_gifts.suite,
    test_gifts_tooltip.suite,
    test_music_gifts.suite,
    test_progressive_scroll.suite,
    test_gifts_sections_list.suite,
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)
