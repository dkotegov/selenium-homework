import os

browser = os.environ.get('BROWSER', 'firefox')

SELENIUM_EX = {
    'USE_REMOTE': True,
    'MAXIMIZE_WINDOW': True,
    'DEFAULT_BROWSER': browser,
    'PROJECT_URL': 'https://www.ok.ru/',
    'PAGE_LOAD_TIMEOUT': 60,

    'REMOTE': {
        'command_executor': 'http://192.168.238.128:4444/wd/hub',
    }
}