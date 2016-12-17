import os

import seismograph

import utils
from pages.auth_page import AuthPage


class BaseCase(seismograph.Case):

    def setup(self):
        self.selenium = self.ext('selenium')
        self.selenium.start()
        self.browser = self.selenium.browser
        auth_page = AuthPage(self.browser)
        auth_page.open()
        auth_page.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
        self.browser.waiting_for(lambda: not self.browser.title.startswith(auth_page.TITLE))

    def teardown(self):
        self.browser.quit()
