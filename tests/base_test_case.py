# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects import AuthPage


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        BROWSER = os.environ.get('BROWSER', 'FIREFOX')

        self.username = os.environ.get('OKRU_USERNAME')
        self.login = os.environ['OKRU_LOGIN']
        self.password = os.environ['OKRU_PASSWORD']

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, BROWSER).copy()
        )
        self.is_logged = self.auth()

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.set_username(self.username)
        auth_form.set_login(self.login)
        auth_form.set_password(self.password)
        auth_form.submit()
        return auth_form.is_logged
