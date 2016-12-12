import os
import random

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

    # ATTACH_BUTTON_TRIG = '//span[@class="comments_attach_trigger"]'
    # ATTACH_AUDIO_MSG_BUTTON = '//span[@class="comments_attach_trigger"]/div[2]/div/div/ul/li[1]'
    # AUDIO_MSG_POPUP = '//object[@class="vchat_flash_app"]'
    # PLAY_BUTTON = '//div[@class="msg_audio"]/div[@class="msg_audio_play"]/'#/div[last()]/div[@class="msg_cnt"]'#/div[]/div[@class="js-msg-attach"]/div/div'

    def get_button_send(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEND_MSG_BTN)
        )
        self.driver.find_element_by_xpath(self.SEND_MSG_BTN).click()

    def set_message(self, message):
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(message)

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
        rand = random.random() * 10**10
        message = str(rand)
        self.message_page.open()
        self.message_page.messages_menu.set_message(message)
        self.message_page.messages_menu.get_button_send()


