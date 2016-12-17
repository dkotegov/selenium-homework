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

    def send_message(self):
        self.driver.find_element_by_css_selector('.itx').send_keys("Тестовое сообщение")
        self.driver.find_element_by_css_selector('.comments_add-controls_save').click()

    def get_text_from_input(self):
        return self.driver.find_element_by_css_selector('.itx').text

    def report_msg(self):
        self.driver.find_element_by_css_selector('.ic10_warn-g').click()

    def get_report_popup(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.modal-new_cnt')
        )


class GroupMessagesTest(unittest.TestCase):
    USERS_COUNT = u'3 участника'

    def setUp(self):
        browser = 'FIREFOX'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Auth here
        auth_page.authorize()

    def tearDown(self):
        self.driver.quit()

    def test(self):

        message_page = GroupMessagesPage(self.driver)  # Go to messages
        message_page.open()

        users_count = message_page.messages_menu.get_users_count() # проверка на правильное количество участников
        self.assertEqual(self.USERS_COUNT, users_count)

        message_page.messages_menu.send_message()
        self.assertEqual(message_page.messages_menu.get_text_from_input(), '')  # отправка сообщений

        message_page.messages_menu.report_msg()
        report_window = message_page.messages_menu.get_report_popup()
        self.assertTrue(report_window, not None) # проверка появления попапа о репорте




