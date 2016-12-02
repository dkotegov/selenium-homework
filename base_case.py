import os
import unittest

import selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import utils
from pages.auth_page import AuthPage

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Firefox(capabilities=firefox_capabilities)
        page = AuthPage(self.driver)
        page.open()
        auth_form = page.form
        auth_form.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
        utils.wait(self.driver, lambda d: not d.title.startswith(page.TITLE))

    def tearDown(self):
        self.driver.quit()
