import os

browser = os.environ.get('BROWSER', 'CHROME')

SELENIUM_EX = {
    'USE_REMOTE': True,
    'MAXIMIZE_WINDOW': True,
    'DEFAULT_BROWSER': browser,
    'PROJECT_URL': 'https://www.ok.ru/',
    'PAGE_LOAD_TIMEOUT': 60,
    'REMOTE': {
        'command_executor': 'http://127.0.0.1:4444/wd/hub',
    }
}