# -*- coding: utf-8 -*-
import os

import unittest
import settings
from BasicMethods import Page, Component, AuthPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class GroupMessagesPage(Page):
    BASE_URL = 'https://ok.ru/messages/c68009778785062'

    @property
    def messages_menu(self):
        return MessagesMenu(self.driver)


class MessagesMenu(Component):
    ATTACH_BUTTON_TRIG = '//span[@class="comments_attach_trigger"]'
    ATTACH_VIDEOMSG_BUTTON = '//span[@class="comments_attach_trigger"]/div[2]/div/div/ul/li[1]'
    VIDEOMSG_POPUP = '//span[@id="hook_Modal_popLayerModal"]'

    def get_button_attach(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ATTACH_BUTTON_TRIG)
        )
        self.driver.find_element_by_xpath(self.ATTACH_BUTTON_TRIG).click()

    def get_button_videomessage(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ATTACH_VIDEOMSG_BUTTON)
        )
        self.driver.find_element_by_xpath(self.ATTACH_VIDEOMSG_BUTTON).click()

    def get_videomessage_popup(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.VIDEOMSG_POPUP)
        )


class AudioMessagesTest(unittest.TestCase):
    USERS_COUNT = u'3 участника'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Auth here
        auth_page.authorize()

    def tearDown(self):
        self.driver.quit()

    def test_videomessage_window_opens(self):
        message_page = GroupMessagesPage(self.driver)  # Go to messages
        message_page.open()

        message_page.messages_menu.get_button_attach()

        message_page.messages_menu.get_button_videomessage()

        videomsg_popup = message_page.messages_menu.get_videomessage_popup()
        self.assertIsNotNone(videomsg_popup)