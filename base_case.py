import os
import unittest

import selenium
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import DesiredCapabilities, Remote

import utils
from pages.auth_page import AuthPage

# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True

class BaseCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        #self.driver = selenium.webdriver.Firefox(capabilities=firefox_capabilities)
        page = AuthPage(self.driver)
        page.open()
        auth_form = page.form
        auth_form.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
        utils.wait(self.driver, lambda d: not d.title.startswith(page.TITLE))

    def tearDown(self):
        self.driver.quit()
