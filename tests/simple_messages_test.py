import os
import random
import time

import unittest
import settings
from time import sleep
from BasicMethods import Page, Component, AuthPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class SimpleMessagesPage(Page):
    BASE_URL = 'https://ok.ru/messages/589325601321'

    @property
    def messages_menu(self):
        return MessagesMenu(self.driver)


class MessagesMenu(Component):
    SEND_MSG_BTN = '//button[@class="button-pro comments_add-controls_save"]'
    MESSAGE = '//div[@name="st.txt"]'
    EDITTED = '//a[@class="msg_ac_i ic10 ic10_edit foh-s js-msg-edit"]'

    def get_button_send(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEND_MSG_BTN)
        )
        self.driver.find_element_by_xpath(self.SEND_MSG_BTN).click()

    def set_message(self, message):
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(message)

    def get_message(self):
        return self.driver.find_element_by_xpath(self.MESSAGE)

    def edit_message(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITTED)
        )
        self.driver.find_element_by_xpath(self.EDITTED).click()

class SimpleMessagesTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Auth here
        auth_page.authorize()

        self.message_page = SimpleMessagesPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_send_simple_message(self):
        message = 'test'
        self.message_page.open()
        self.message_page.messages_menu.set_message(message)
        self.message_page.messages_menu.get_button_send()
        input_pole = self.message_page.messages_menu.get_message().text
        self.assertEqual(input_pole, '')

    def test_edit_simple_message(self):
        message = 'testEdit'
        self.message_page.open()
        self.message_page.messages_menu.edit_message()
        self.message_page.messages_menu.set_message(message)
        self.message_page.messages_menu.get_button_send()
        input_pole = self.message_page.messages_menu.get_message().text
        self.assertEqual(input_pole, '')