# -*- coding: utf-8 -*-
from .base import Component, Page
import utils
from urlparse import urlsplit
from channel_page import ChannelPage


class MyVideosPage(Page):
    PATH = 'video/myVideo'
    MAIN_CREATE_CHANNEL_ID = 'vv_btn_create_channel_main'

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

    def create_channel_click(self):
        utils.wait_id(self.driver, self.MAIN_CREATE_CHANNEL_ID).click()
        return CreateChannelDialog(self.driver)

    def create_channel(self, name):
        create_channel_dialog = self.create_channel_click()
        create_channel_dialog.set_channel_name(name)
        return create_channel_dialog.submit()


class VideoActionList(Component):
    CREATE_CHANNEL_ID = 'vv_btn_create_channel_left_menu'

    def create_channel(self):
        utils.wait_id(self.driver, self.CREATE_CHANNEL_ID).click()
        return CreateChannelDialog(self.driver)


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
