import os

import unittest
import settings
from time import sleep
from BasicMethods import Page, Component, AuthPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class GroupMessagesPage(Page):
    BASE_URL = 'https://ok.ru/messages/589325601321'

    @property
    def messages_menu(self):
        return MessagesMenu(self.driver)


class MessagesMenu(Component):
    ATTACH_BUTTON_TRIG = '//span[@class="comments_attach_trigger"]'
    ATTACH_AUDIO_MSG_BUTTON = '//span[@class="comments_attach_trigger"]/div[2]/div/div/ul/li[1]'
    AUDIO_MSG_POPUP = '//object[@class="vchat_flash_app"]'
    PLAY_BUTTON = '//div[@class="msg_audio"]/div[@class="msg_audio_play"]/'#/div[last()]/div[@class="msg_cnt"]'#/div[]/div[@class="js-msg-attach"]/div/div'

    def get_users_count(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERS_COUNT).text
        )

class SimpleMessagesTest(unittest.TestCase):
    USERS_COUNT = u'2 участника'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Auth here
        auth_page.authorize()

        self.message_page = GroupMessagesPage(self.driver)


