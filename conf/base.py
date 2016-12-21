# -*- coding: utf-8 -*-

import os
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options as ChromeOptions


conf_path = os.path.dirname(__file__)

project_path = conf_path.replace(conf_path.split('/')[-1], '')

STATIC_PATH = '{0}static/'.format(project_path)


OK_URL = 'http://ok.ru/'
OK_USER_ID = 'prostok0smos'

USERNAME = os.environ.get('USERNAME', '')
PASSWORD = os.environ.get('PASSWORD', '')


chrome_options = ChromeOptions()
chrome_options.add_argument('disable-geolocation')

firefox_profile = FirefoxProfile()
firefox_profile.set_preference('geo.prompt.testing', True)
firefox_profile.set_preference('geo.prompt.testing.allow', True)


SELENIUM_EX = {
    'USE_REMOTE': os.environ.get('USE_REMOTE', True),
    'REMOTE': {
        'command_executor': 'http://127.0.0.1:4444/wd/hub',
    },

    'PROJECT_URL': '{0}{1}/'.format(OK_URL, OK_USER_ID),

    'POLLING_TIMEOUT': 10,

    'DEFAULT_BROWSER': os.environ.get('BROWSER', 'CHROME'),
    'MAXIMIZE_WINDOW': True,

    'CHROME': {
        'executable_path': '{0}drivers/chromedriver'.format(project_path),
        'chrome_options': chrome_options
    },

    'FIREFOX': {
        'firefox_profile': firefox_profile
    }
}
