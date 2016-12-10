import os

BROWSER = 'FIREFOX'
LOGIN = 'technopark16'
PASSWORD = 'testQA1'

class Settings:

    def __init__(self):
        pass

    @staticmethod
    def get_browser():
        browser = BROWSER
        if os.environ['BROWSER'] == 'CHROME' or os.environ['BROWSER'] == 'FIREFOX':
            browser = os.environ['BROWSER']
        return browser

    @staticmethod
    def get_login():
        return LOGIN

    @staticmethod
    def get_password():
        return PASSWORD
