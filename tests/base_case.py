# -*- coding: utf-8 -*-

import os
import seismograph
from selenium.webdriver import DesiredCapabilities, Remote
from test_auth import AuthPage


class BaseCase(seismograph.Case):
    USERLOGIN = os.environ['LOGIN']
    USERNAME = u'Евдакия Фёдорова'
    PASSWORD = os.environ['PASSWORD']

    def setup(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERLOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.user_block.get_username()
        self.assertion.equal(user_name, self.USERNAME)

    def teardown(self):
        self.driver.quit()
