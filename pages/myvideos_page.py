# -*- coding: utf-8 -*-
from seismograph.ext import selenium

import utils
from utils import query


class VideoActionList(selenium.PageItem):
    create_channel_button = query('A', _id='vv_btn_create_channel_left_menu')


class CreateChannelDialog(selenium.PageItem):
    channel_name_input = query("INPUT", name='st.vv_albumName')
    submit_button = query("INPUT", value=u'Создать канал')

    def create_channel(self, name):
        self.channel_name_input.set(name)
        self.submit_button.click()
        utils.wait_change_url(self.browser)


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
