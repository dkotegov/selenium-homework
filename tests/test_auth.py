# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from test_base import Page
from test_base import Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def user_block(self):
        return UserBlock(self.driver)


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
