import os
import unittest

import selenium

import utils
from pages.auth_page import AuthPage


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Firefox()
        page = AuthPage(self.driver)
        page.open()
        auth_form = page.form
        auth_form.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
        utils.wait(self.driver, lambda d: not d.title.startswith(page.TITLE))
    def tearDown(self):
        self.driver.quit()