# -*- coding: utf-8 -*-
from .base import Component, Page
import utils
from urlparse import urlsplit
from channel_page import ChannelPage
from seismograph.ext import selenium
from utils import query

class VideoActionList(selenium.PageItem):
    create_channel_button = query( 'A', _id ='vv_btn_create_channel_left_menu')


class CreateChannelDialog(selenium.PageItem):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Создать канал"]'

    channel_name_input = query("INPUT", name = 'st.vv_albumName')
    submit_button =  query("INPUT", value = u'Создать канал')

    def create_channel(self, name):
        self.channel_name_input.set(name)
        self.submit_button.click()
        utils.wait_change_url(self.browser)

    def set_channel_name(self, name):
        utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH).send_keys(name)

    def submit(self):
        utils.wait_xpath(self.driver, self.CHANNEL_SUBMIT_XPATH).click()
        utils.wait_change_url(self.driver)
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page

class MyVideosPage(selenium.Page):
    __url_path__ = '/video/myVideo'

    main_create_channel_button = query('A', _id='vv_btn_create_channel_main')
    action_list = selenium.PageElement(VideoActionList)
    create_channel_dialog = selenium.PageElement(CreateChannelDialog)

    def create_channel_left_menu(self, name):
        self.action_list.create_channel_button.click()
        self.create_channel_dialog.create_channel(name)

    def create_channel(self, name):
        self.main_create_channel_button.click()
        self.create_channel_dialog.create_channel(name)



