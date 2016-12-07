# -*- coding: utf-8 -*-
import os

import unittest
import urlparse
from BasicMethods import Page, Component, AuthPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class GroupMessagesTest(unittest.TestCase):
    def setUp(self):
        browser = 'FIREFOX'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login('technopark16')
        auth_form.set_password('testQA1')
        auth_form.submit()

        self.assertEqual('technopark16 technopark16', '123')
