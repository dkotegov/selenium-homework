# -*- coding: utf-8 -*-

import seismograph


__all__ = [
    'program'
]


program = seismograph.Program(config_path='conf.base', require=['selenium'])
