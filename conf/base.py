# -*- coding: utf-8 -*-

import os
from selenium.webdriver.chrome.options import Options


conf_path = os.path.dirname(__file__)

project_path = conf_path.replace(conf_path.split('/')[-1], '')

STATIC_PATH = '{0}static/'.format(project_path)

OK_URL = 'http://ok.ru/'
OK_USER_ID = 'prostok0smos'


chrome_options = Options()
chrome_options.add_argument('disable-geolocation')

SELENIUM_EX = {
    'PROJECT_URL': '{0}{1}/'.format(OK_URL, OK_USER_ID),

    'POLLING_TIMEOUT': 15,

    'DEFAULT_BROWSER': 'chrome',
    'MAXIMIZE_WINDOW': True,
    # 'LOGS_PATH': '/var/log/selenium-homework.log',

    'CHROME': {
        'executable_path': '{0}drivers/chromedriver'.format(project_path),
        'chrome_options': chrome_options
    }
}
