# -*- coding: utf-8 -*-
import os

import unittest
import settings
from time import sleep
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
    VIDEOMSG_POPUP = '//object[@class="vchat_flash_app"]'
    PLAY_BUTTON = '//div[@class="msg_audio"]/div[@class="msg_audio_play"]/'#/div[last()]/div[@class="msg_cnt"]'#/div[]/div[@class="js-msg-attach"]/div/div'
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

    def click_play_button(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.msg_audio:last-child')
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

        self.message_page = GroupMessagesPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    #def test_audiomessage_window_opens(self):
         # Go to messages
        #self.message_page.open()
        # self.message_page.messages_menu.get_button_attach()
        #
        # self.message_page.messages_menu.get_button_videomessage()
        #
        # videomsg_popup = self.message_page.messages_menu.get_videomessage_popup()
        # #проверяем выскочил ли object с флешом
        # self.assertIsNotNone(videomsg_popup)

    def test_audiomessage_play_message(self):
        self.message_page.open()
        self.message_page.messages_menu.click_play_button()
        last_audio_msg = self.driver.find_element_by_css_selector('.msg_audio:last-child')
        dfdf = self.driver.find_elements_by_xpath('//div[@class="msg_audio"]')
        aaaaaaa = last_audio_msg.find_element_by_xpath('//div[@class="msg_audio_play"]')
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_elements_by_xpath('//div[@class="msg_audio_play"]')
        )

        aaaaaaa.click()
        #sleep(1)
        classname_last_audio_msg = last_audio_msg.get_attribute("class")
        self.assertTrue(classname_last_audio_msg.rfind("st_play") != -1)