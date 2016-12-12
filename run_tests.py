# -*- coding: utf-8 -*-

from tests.notes import test_create
from tests.notes import test_restore
from tests.notes import test_in_status
from tests.notes import test_rate

import seismograph


suites = (
    test_create.suite,
    test_restore.suite,
    test_in_status.suite,
    test_rate.suite
)


program = seismograph.Program(config_path='conf.base', require=['selenium'], suites=suites)


if __name__ == '__main__':
    program()
