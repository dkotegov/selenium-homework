# -*- coding: utf-8 -*-

import sys

from tests.car_showrooms.add_showroom_test import AddShowroomFormTest
from tests.car_showrooms.list_showroom_test import ShowroomListTest
from tests.car_showrooms.list_special_offers_test import SpecialOffersListTest
from tests.car_showrooms.search_showroom_tests import *

if __name__ == '__main__':

    suite = unittest.TestSuite((
        unittest.makeSuite(RegionSelectFormTest),
        unittest.makeSuite(SelectCarModelTest),
        unittest.makeSuite(SelectStationTest),
        unittest.makeSuite(IsOfficialCheckboxTest),
        unittest.makeSuite(SearchFormTest),
        unittest.makeSuite(ShowroomListTest),
        unittest.makeSuite(SpecialOffersListTest),
        unittest.makeSuite(AddShowroomFormTest),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
