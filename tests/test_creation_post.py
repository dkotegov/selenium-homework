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


class ExampleTest(#seismograph.Case):
    unittest.TestCase):

    USERLOGIN = 'technopark30'
    USERNAME = u'Евдакия Фёдорова'
    PASSWORD = os.environ.get('PASSWORD', 'testQA1')

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
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
        auth_form.open_form()
        auth_form.set_login(self.USERLOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.user_block.get_username()
        self.assertEqual(user_name, self.USERNAME)

