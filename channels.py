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
    VIDEO_URL_STUB = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    VIDEO_NAME_STUB = 'Rick Astley - Never Gonna Give You Up'
    NEW_VIDEO_NAME_STUB = 'NEW_VIDEO_NAME_STUB'
    NEW_DESCRIPTION_STUB = 'NEW_DESCRIPTION_STUB'
    NEW_TAGS_STUB = 'tag tag2'

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

    def test_add_video(self):
        self.channel_page.add_video_by_url(self.VIDEO_URL_STUB)
        self.assertIn(self.VIDEO_NAME_STUB, self.driver.page_source)#TODO Проверять по-другому
        self.channel_page.delete_video()
        self.channel_page.open()
        self.assertNotIn(self.VIDEO_NAME_STUB, self.driver.page_source)

    def test_change_video_name(self):
        self.channel_page.add_video_by_url(self.VIDEO_URL_STUB)
        self.channel_page.edit_video(self.NEW_VIDEO_NAME_STUB)
        self.assertIn(self.NEW_VIDEO_NAME_STUB, self.driver.page_source)
        self.channel_page.edit_video(self.VIDEO_NAME_STUB)
        self.channel_page.delete_video()



    def tearDown(self):
        self.channel_page.delete_channel()
        super(ChangeChannelCase, self).tearDown()

