import seismograph
import os
from seismograph.ext import selenium
from pages.auth_page import AuthPage
#suite = seismograph.Suite(__name__, require=['selenium'])
import utils
#selenium = suite.ext('selenium')




class BaseCase(seismograph.Case):
    def setup(self):
        try:
            self.selenium =self.ext('selenium')
            self.selenium.start()
            self.browser = self.selenium.browser
            auth_page = AuthPage(self.browser)
            auth_page.open()
            auth_page.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
            utils.wait(self.browser, lambda d: not d.title.startswith(auth_page.TITLE))
        except:#TODO
            self.browser.quit()

    def teardown(self):
        self.browser.quit()
        #self.driver.quit()
