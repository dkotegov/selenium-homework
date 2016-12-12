# -*- coding: utf-8 -*-

from tests.notes import test_create
from tests.notes import test_restore

import seismograph


suites = (
    test_create.suite,
    test_restore.suite,
)


program = seismograph.Program(config_path='conf.base', require=['selenium'], suites=suites)


if __name__ == '__main__':
    program()
