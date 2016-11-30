# -*- coding: utf-8 -*-

import unittest
from urlparse import urlsplit, urljoin
import utils
import os

from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''
    TITLE = 'OK.RU'

    @property
    def form(self):
        return AuthForm(self.driver)

class MyVideosPage(Page):
    PATH = 'video/myVideo'

    @property
    def action_list(self):
        return VideoActionList(self.driver)

    @property
    def create_channel_dialog(self):
        return CreateChannelDialog(self.driver)

    def create_channel_left_menu(self, name):
        create_channel_dialog = self.action_list.create_channel()
        create_channel_dialog.set_channel_name(name)
        return create_channel_dialog.submit()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//*[@class="button-pro form-actions_yes"]'  # TODO

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def signin(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.submit()


class VideoActionList(Component):
    CREATE_CHANNEL_ID = 'vv_btn_create_channel_left_menu'

    def create_channel(self):
        utils.wait_id(self.driver, self.CREATE_CHANNEL_ID).click()
        return CreateChannelDialog(self.driver)


class ChannelPage(Page):
    DELETE_BUTTON_CLASS = 'vl_ic_delete'
    CONFIRM_DELETE_XPATH ='//input[@value="Удалить"]'

    def __init__(self, driver, path):
        super(ChannelPage, self).__init__(driver)
        self.path = path

    def delete_channel(self):
        utils.wait_class(self.driver, self.DELETE_BUTTON_CLASS).click()
        confirm_delete =  utils.wait_xpath(self.driver,self.CONFIRM_DELETE_XPATH)
        confirm_delete.click()
        utils.wait_change_url(self.driver)



class CreateChannelDialog(Component):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Создать канал"]'

    def set_channel_name(self, name):
        utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH).send_keys(name)

    def submit(self):
        utils.wait_xpath(self.driver, self.CHANNEL_SUBMIT_XPATH).click()
        utils.wait_change_url(self.driver)
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page
        #self.driver.find_element_by_xpath(self.CHANNEL_SUBMIT_XPATH).click()


class AuthCase(unittest.TestCase):
    CHANEL_NAME_STUB = "LLOLOLOLOLOLOLOL()!()(!)(!)(1!)(!)"

    def setUp(self):
        # browser = os.environ.get('BROWSER', 'FIREFOX') TODO
        self.driver = selenium.webdriver.Firefox()
        page = AuthPage(self.driver)
        page.open()
        auth_form = page.form
        auth_form.signin(os.environ['LOGIN'], os.environ['PASSWORD'])
        self.driver.implicitly_wait(0.5)
        utils.wait(self.driver, lambda d: not d.title.startswith(page.TITLE))


    def tearDown(self):
        self.driver.quit()

    def test_create_from_left_menu(self):
        video_page = MyVideosPage(self.driver)
        video_page.open()
        channel_page = video_page.create_channel_left_menu(self.CHANEL_NAME_STUB)
        self.assertIn(self.CHANEL_NAME_STUB, self.driver.page_source)
        channel_page.delete_channel()
        self.assertNotIn(self.CHANEL_NAME_STUB, self.driver.page_source)

