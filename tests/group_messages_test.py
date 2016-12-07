# -*- coding: utf-8 -*-
import os

import unittest
import urlparse
from BasicMethods import Page, Component, AuthPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class GroupMessagesPage(Page):
    BASE_URL = 'https://ok.ru/messages/c68009778785062'

    @property
    def messages_menu(self):
        return MessagesMenu(self.driver)

class MessagesMenu(Component):
    USERS_COUNT = '//span[@class="js-participants-count"]'

    def get_users_count(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERS_COUNT).text
        )

class GroupMessagesTest(unittest.TestCase):
    USERS_COUNT = u'3 участника'

    def setUp(self):
        browser = 'FIREFOX'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver) # Auth here
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login('technopark16')
        auth_form.set_password('testQA1')
        auth_form.submit()

        message_page = GroupMessagesPage(self.driver) # Go to messages
        message_page.open()

        users_count = message_page.messages_menu.get_users_count()
        self.assertEqual(self.USERS_COUNT, users_count)
