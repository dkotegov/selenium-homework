# -*- coding: utf-8 -*-
import os


project_path = os.path.dirname(__file__)


SELENIUM_EX = {
    'DEFAULT_BROWSER': 'chrome',
    'MAXIMIZE_WINDOW': True,
    # 'LOGS_PATH': '/var/log/selenium-homework.log',

    'CHROME': {
        'executable_path': '{0}/../drivers/chromedriver'.format(project_path),
    }
}


OK_URL = 'http://ok.ru/'
