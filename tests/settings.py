import os

BROWSER = 'FIREFOX'


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
        try:
            LOGIN = os.environ['LOGIN']
            return LOGIN
        except KeyError:
            raise Exception('No login provided')

    @staticmethod
    def get_password():
        try:
            PASSWORD = os.environ['PASSWORD']
            return PASSWORD
        except KeyError:
            raise Exception('No password provided')

