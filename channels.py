# -*- coding: utf-8 -*-
from base_case import BaseCase

from pages.myvideos_page import MyVideosPage

from time import time


class CreateChannelCase(BaseCase):
    def setUp(self):
        super(CreateChannelCase, self).setUp()
        self.channel_name = '{}_{}'.format(time(), id(self.driver))  # TODO Доработать
        self.video_page = MyVideosPage(self.driver)
        self.video_page.open()

    def test_create(self):
        channel_page = self.video_page.create_channel(self.channel_name)
        self.assertIn(self.channel_name, self.driver.page_source)
        channel_page.delete_channel()
        self.assertNotIn(self.channel_name, self.driver.page_source)

    def test_create_from_left_menu(self):
        channel_page = self.video_page.create_channel_left_menu(self.channel_name)
        self.assertIn(self.channel_name, self.driver.page_source)
        channel_page.delete_channel()
        self.assertNotIn(self.channel_name, self.driver.page_source)


class ChangeChannelCase(BaseCase):
    def setUp(self):
        super(ChangeChannelCase, self).setUp()
        self.channel_name = '{}_{}'.format(time(), id(self.driver))  # TODO Доработать
        self.video_page = MyVideosPage(self.driver)
        self.video_page.open()
        self.channel_page = self.video_page.create_channel(self.channel_name)

    def test_change_channel_name(self):
        self.new_name = 'new'
        self.channel_page = self.channel_page.edit_channel(self.new_name)
        self.assertEqual(self.channel_page.channel_name(), self.new_name)

    def tearDown(self):
        self.channel_page.delete_channel()
        super(ChangeChannelCase, self).tearDown()
