# -*- coding: utf-8 -*-
from base_case import BaseCase

from pages.channel_page import ChannelPage
from pages.video_page import VideoPage
from pages.myvideos_page import MyVideosPage


# class CreateChannelCase(BaseCase):
#     TEST_CHANNEL1 = 'TEST_CHANNEL1'
#     TEST_CHANNEL2 = 'TEST_CHANNEL2'
#
#     def setUp(self):
#         super(CreateChannelCase, self ).setUp()
#         self.video_page = MyVideosPage(self.driver)
#         self.video_page.open()
#
#     def test_create(self):
#         channel_page = self.video_page.create_channel(self.TEST_CHANNEL1)
#         self.assertIn(self.TEST_CHANNEL1, self.driver.page_source)
#         channel_page.delete_channel()
#         self.assertNotIn(self.TEST_CHANNEL1, self.driver.page_source)
#
#     def test_create_from_left_menu(self):
#         channel_page = self.video_page.create_channel_left_menu(self.TEST_CHANNEL2)
#         self.assertIn(self.TEST_CHANNEL2, self.driver.page_source)
#         channel_page.delete_channel()
#         self.assertNotIn(self.TEST_CHANNEL2, self.driver.page_source)


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

    TEST_RENAME_VIDEO_LINK = 'video/c1533928'
    VIDEO_TO_RENAME = 'video/202886615528'
    NEW_VIDEO_NAME = NEW_VIDEO_NAME_STUB


    def test_move_video(self):
        DESTINATION_LINK = 'video/c1534952'
        SOURCE_LINK = 'video/c1535208'
        DESTINATION_NAME ='DESTINATION_CHANNEL'
        SOURCE_NAME = 'SOURCE_CHANNEL'
        VIDEO_NAME = 'VIDEO_TO_MOVE'
        source = ChannelPage(self.driver,SOURCE_LINK)
        destination = ChannelPage(self.driver,DESTINATION_LINK)
        source.open()
        source.move_video(VIDEO_NAME, DESTINATION_NAME)
        self.assertNotIn(VIDEO_NAME, source.get_videos_titles())
        destination.open()
        self.assertIn(VIDEO_NAME, destination.get_videos_titles())
        destination.move_video(VIDEO_NAME, SOURCE_NAME)

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
            video_page  = VideoPage(self.driver, self.VIDEO_TO_RENAME)
            video_page.open()
            self.assertEquals(self.NEW_VIDEO_NAME_STUB, video_page.title)
            channel_page.open()
        finally:
            channel_page.edit_video(self.NEW_VIDEO_NAME_STUB,title=self.VIDEO_NAME_STUB)

    def test_change_video_name(self):
        OLD_DESCRIPTION = 'OLD_DESCRIPTION'
        NEW_DESCRIPTION = 'NEW_DESCRIPTION'
        CHANNEL_LINK = 'video/c1534440'
        VIDEO_LINK = 'video/202962440680'
        channel_page = ChannelPage(self.driver, CHANNEL_LINK)
        try:
            channel_page.open()
            channel_page.edit_video( self.VIDEO_NAME_STUB, description = NEW_DESCRIPTION)
            video_page  = VideoPage(self.driver, VIDEO_LINK)
            video_page.open()
            self.assertEquals(NEW_DESCRIPTION, video_page.description)#TODO
            channel_page.open()
        finally:
            channel_page.edit_video(self.VIDEO_NAME_STUB,description=OLD_DESCRIPTION)

class SubscriptionsCase(BaseCase):
    CHANNEL_LINK =  'video/c1100320'
    VIDEO_LINK = 'video/203665445152'

    def test_subscribe_from_channel_page(self):
        channel_page = ChannelPage(self.driver, self.CHANNEL_LINK)
        channel_page.open()
        channel_page.subscribe()
        self.assertTrue(channel_page.is_subscribe() )
        channel_page.unsubscribe()
        self.assertTrue(channel_page.is_not_subscribe() )#TODO

    def test_subscribe_from_video_page(self):
        video_page = VideoPage(self.driver, self.VIDEO_LINK)
        video_page.open()
        video_page.subscribe()
        self.assertTrue(video_page.is_subscribe())
        video_page.unsubscribe()
        self.assertTrue(video_page.is_not_subscribe())  # TODO



