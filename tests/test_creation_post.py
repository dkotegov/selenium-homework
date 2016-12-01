# -*- coding: utf-8 -*-

import os

import unittest
# import seismograph
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def user_block(self):
        return UserBlock(self.driver)

class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):

    LOGIN_BUTTON = "//a[@id='enterHeader']"
    LOGIN = "//input[@id='field_email']"
    PASSWORD = "//input[@id='field_password']"
    SUBMIT = "//input[@value='Войти']"

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class UserBlock(Component):

    USERNAME = "//div[@class='mctc_nameAndOnline']/span[@class='mctc_name textWrap']/a[@class='mctc_nameLink']" \
               "/h1[@class='mctc_name_tx bl']"

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )

class GroupPage(Page):

    PATH = "/group/53389738115166"
    CREATE_POST = "//div[@class='input_placeholder']"

    @property
    def creating_post(self):
        self.driver.find_element_by_xpath(self.CREATE_POST).click()
        return NewPost(self.driver)
    @property
    def get_last_post(self):
        return LastPost(self.driver)


class NewPost(Component):
    TEXT_POST = "//div[@id='posting_form_text_field']"
    SUBMIT = "//input[@value='Поделиться'][@class='button-pro']"

    def set_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT_POST)
        )
        self.driver.find_element_by_xpath(self.TEXT_POST).click()
        self.driver.find_element_by_xpath(self.TEXT_POST).send_keys(text)

    def submit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class LastPost(Component):
    LAST_POST = "//div[@class='media-text_cnt']//div[@class='media-text_cnt_tx textWrap']"

    def is_last_post_new_post(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_POST).text == text
        )
        return True

    # def delete(self):


class CreationPostTest(#seismograph.Case):
    unittest.TestCase):
    USERLOGIN = 'technopark30'
    USERNAME = u'Евдакия Фёдорова'
    PASSWORD = os.environ.get('PASSWORD', 'testQA1')
    # new_post = NewPost
    group_page = GroupPage

    def setUp(self):
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
        self.assertEqual(user_name, self.USERNAME)

        self.group_page = GroupPage(self.driver)
        self.group_page.open()
        self.new_post = self.group_page.creating_post


    def tearDown(self):
        self.driver.quit()

    def test(self):
        text = "simple post with simple text666"

        new_post = self.group_page.creating_post
        new_post.set_text(text)
        new_post.submit()
        last_post = self.group_page.get_last_post
        self.assertTrue(last_post.is_last_post_new_post(text))






