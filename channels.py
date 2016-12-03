# -*- coding: utf-8 -*-
from base_case import BaseCase

from pages.channel_page import ChannelPage
from pages.myvideos_page import MyVideosPage


class CreateChannelCase(BaseCase):
    TEST_CHANNEL1 = 'TEST_CHANNEL1'
    TEST_CHANNEL2 = 'TEST_CHANNEL2'

    def setUp(self):
        self.video_page = MyVideosPage(self.driver)
        self.video_page.open()

    def test_create(self):
        channel_page = self.video_page.create_channel(self.TEST_CHANNEL1)
        self.assertIn(self.TEST_CHANNEL1, self.driver.page_source)
        channel_page.delete_channel()
        self.assertNotIn(self.TEST_CHANNEL1, self.driver.page_source)

    def test_create_from_left_menu(self):
        channel_page = self.video_page.create_channel_left_menu(self.TEST_CHANNEL2)
        self.assertIn(self.TEST_CHANNEL2, self.driver.page_source)
        channel_page.delete_channel()
        self.assertNotIn(self.TEST_CHANNEL2, self.driver.page_source)


class ChangeChannelCase(BaseCase):
    VIDEO_URL_STUB = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    VIDEO_NAME_STUB = 'Rick Astley - Never Gonna Give You Up'
    NEW_VIDEO_NAME_STUB = 'NEW_VIDEO_NAME_STUB'
    NEW_DESCRIPTION_STUB = 'NEW_DESCRIPTION_STUB'
    NEW_TAGS_STUB = 'tag tag2'
    TEST_RENAME_LINK = '/video/c1534696'
    CHANNEL_NAME = 'TEST_RENAME'
    NEW_CHANNEL_NAME = 'NEWNAME'

    TEST_ADD_VIDEO_LINK = '/video/c1533672'

    TEST_RENAME_VIDEO_LINK = ''
    NEW_VIDEO_NAME = NEW_VIDEO_NAME_STUB




    def test_rename_channel(self):
        channel_page = ChannelPage(self.driver, self.TEST_RENAME_LINK)
        try:
            channel_page.open()
            channel_page.edit_channel(self.NEW_CHANNEL_NAME)
            self.assertEqual(channel_page.channel_name(), self.NEW_CHANNEL_NAME)
        finally:
            channel_page.edit_channel(self.CHANNEL_NAME)

    def test_add_video(self):
        channel_page = ChannelPage(self.driver, self.TEST_ADD_VIDEO_LINK)
        channel_page.open()
        channel_page.add_video_by_url(self.VIDEO_URL_STUB)
        self.assertIn(self.VIDEO_NAME_STUB, channel_page.get_videos_titles())
        channel_page.delete_video_by_name(self.VIDEO_NAME_STUB)
        self.assertNotIn(self.VIDEO_NAME_STUB, channel_page.get_videos_titles())

    def test_change_video_name(self):
        channel_page = ChannelPage(self.driver, self.TEST_RENAME_VIDEO_LINK)
        try:
            channel_page.open()
            channel_page.edit_video(self.VIDEO_NAME_STUB, title = self.NEW_VIDEO_NAME_STUB)
            self.assertIn(self.NEW_VIDEO_NAME_STUB,  channel_page.get_videos_titles())#TODO
            channel_page.edit_video(self.NEW_VIDEO_NAME_STUB,title=self.VIDEO_NAME_STUB)
        finally:
            channel_page.delete_video_by_name(self.VIDEO_NAME_STUB)

