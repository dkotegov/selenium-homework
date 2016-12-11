# -*- coding: utf-8 -*-
import os

import seismograph

from tests import test_gifts_sections_list

os.environ['LOGIN'] = 'technopark1'
os.environ['PASSWORD'] = 'passw0rd'

print os.environ['LOGIN']
print os.environ['PASSWORD']


suites = [
    test_gifts_sections_list.suite
]

if __name__ == '__main__':
    seismograph.main(config_path='config.py', suites=suites)
