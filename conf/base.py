# -*- coding: utf-8 -*-
import os


project_path = os.path.dirname(__file__)


OK_URL = 'http://ok.ru/'
OK_USER_ID = 'prostok0smos'


SELENIUM_EX = {
    'PROJECT_URL': '{0}{1}/'.format(OK_URL, OK_USER_ID),

    'POLLING_TIMEOUT': 15,

    'DEFAULT_BROWSER': 'chrome',
    'MAXIMIZE_WINDOW': True,
    # 'LOGS_PATH': '/var/log/selenium-homework.log',

    'CHROME': {
        'executable_path': '{0}/../drivers/chromedriver'.format(project_path),
    }
}
