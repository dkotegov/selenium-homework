# -*- coding: utf-8 -*-
import os

import unittest
import urlparse

import time
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
    def top_menu(self):
        return TopMenu(self.driver)

    def authorize(self):
        self.open()

        auth_form = self.form
        auth_form.set_login('technopark16')
        auth_form.set_password('testQA1')
        auth_form.submit()
        self.top_menu.get_username() # wait for loading


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@class="button-pro form-actions_yes"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    USERNAME = '//h1[contains(@class, "mctc_name_tx") and contains(@class, "bl")]'
    AVATAR = '//div[@class="card_wrp"]'

    def get_avatar(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            self.driver.find_element_by_xpath(self.AVATAR)
        )

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )
