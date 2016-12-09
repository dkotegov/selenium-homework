# -*- coding: utf-8 -*-
import seismograph

from base_case import BaseCase
from pages.channel_page import ChannelPage
from pages.myvideos_page import MyVideosPage
from pages.video_page import VideoPage

suite = seismograph.Suite(__name__, require=['selenium'])

#@suite.register
class CreateChannelCase(BaseCase):
    TEST_CHANNEL1 = 'TEST_CHANNEL1'
    TEST_CHANNEL2 = 'TEST_CHANNEL2'

    def setup(self):
        super(CreateChannelCase, self ).setup()
        self.video_page = MyVideosPage(self.browser)
        self.video_page.open()
        self.channel_page = ChannelPage(self.browser)

    def test_create(self):
        self.video_page.create_channel(self.TEST_CHANNEL1)
        self.assertion.is_in(self.TEST_CHANNEL1, self.browser.page_source)#TODO использовать список каналов
        self.channel_page.delete_channel()
        self.assertion.is_not_in(self.TEST_CHANNEL1, self.browser.page_source)

    def test_create_from_left_menu(self):
        self.video_page.create_channel_left_menu(self.TEST_CHANNEL2)
        self.assertion.is_in(self.TEST_CHANNEL2, self.browser.page_source)
        self.channel_page.delete_channel()
        self.assertion.is_not_in(self.TEST_CHANNEL2, self.browser.page_source)

@suite.register
class ChangeChannelCase(BaseCase):
    VIDEO_URL_STUB = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    VIDEO_NAME_STUB = 'Rick Astley - Never Gonna Give You Up'
    NEW_VIDEO_NAME_STUB = 'NEW_VIDEO_NAME_STUB'
    NEW_DESCRIPTION_STUB = 'NEW_DESCRIPTION_STUB'
    NEW_TAGS_STUB = 'tag tag2'


    TEST_ADD_VIDEO_LINK = '/video/c1533672'




    # def test_move_video(self):
    #     DESTINATION_ID = '1534952'
    #     SOURCE_ID = '1535208'
    #     DESTINATION_NAME ='DESTINATION_CHANNEL'
    #     SOURCE_NAME = 'SOURCE_CHANNEL'
    #     VIDEO_NAME = 'VIDEO_TO_MOVE'
    #     source = ChannelPage(self.browser)
    #     destination = ChannelPage(self.browser)
    #     source.open(id=SOURCE_ID)
    #     source.move_video(VIDEO_NAME, DESTINATION_NAME)
    #     self.assertion.is_not_in(VIDEO_NAME, source.get_videos_titles())
    #     destination.open(id=DESTINATION_ID)
    #     self.assertion.is_in(VIDEO_NAME, destination.get_videos_titles())
    #     destination.move_video(VIDEO_NAME, SOURCE_NAME)

    # def test_rename_channel(self):#TODO fix
    #     CHANNEL_ID = '1534696'
    #     CHANNEL_NAME = 'TEST_RENAME'
    #     NEW_CHANNEL_NAME = 'NEWNAME'
    #     channel_page = ChannelPage(self.browser)
    #     try:
    #         channel_page.open(id=CHANNEL_ID)
    #         channel_page.edit_channel(NEW_CHANNEL_NAME)
    #         self.assertEqual(channel_page.channel_name, NEW_CHANNEL_NAME)
    #     finally:
    #         channel_page.edit_channel(CHANNEL_NAME)

    # def test_add_video(self):
    #     channel_page = ChannelPage(self.browser, self.TEST_ADD_VIDEO_LINK)
    #     channel_page.open()
    #     channel_page.add_video_by_url(self.VIDEO_URL_STUB)
    #     self.assertIn(self.VIDEO_NAME_STUB, channel_page.get_videos_titles())
    #     channel_page.delete_video_by_name(self.VIDEO_NAME_STUB)
    #     self.assertNotIn(self.VIDEO_NAME_STUB, channel_page.get_videos_titles())
    #
    # def test_add_tags(self):#TODO исправить
    #     CHANNEL_LINK = 'video/c1534184'
    #     NEW_TAG = 'TAGTAGTAG'
    #     VIDEO_NAME = 'VIDEO_TO_TEST_TAGS'
    #     channel_page = ChannelPage(self.browser, CHANNEL_LINK)
    #     channel_page.open()
    #     channel_page.edit_video(VIDEO_NAME, new_tags=NEW_TAG)
    #     self.assertIn(NEW_TAG, channel_page.get_video_tags(VIDEO_NAME))
    #     channel_page.edit_video(VIDEO_NAME, remove_tags=NEW_TAG)
    #     self.assertNotIn(NEW_TAG, channel_page.get_video_tags(VIDEO_NAME))
    #
    # def test_change_video_name(self):
    #     CHANNEL_ID = '1533928'
    #     VIDEO_ID = '202886615528'
    #     NEW_VIDEO_NAME = self.NEW_VIDEO_NAME_STUB
    #     channel_page = ChannelPage(self.browser )
    #     channel_page.open(id=CHANNEL_ID)
    #     channel_page.edit_video(self.VIDEO_NAME_STUB, title=self.NEW_VIDEO_NAME_STUB)
    #     video_page = VideoPage(self.browser)
    #     video_page.open(id=VIDEO_ID)
    #     #utils.wait_change_url(self.browser)
    #     video_title = video_page.title.text
    #     self.assertion.equal(self.NEW_VIDEO_NAME_STUB, video_title)
    #     channel_page.open(id=CHANNEL_ID)
    #     channel_page.edit_video(self.NEW_VIDEO_NAME_STUB, title=self.VIDEO_NAME_STUB)

    def test_change_video_description(self):
        OLD_DESCRIPTION = 'OLD_DESCRIPTION'
        NEW_DESCRIPTION = 'NEW_DESCRIPTION'
        CHANNEL_ID = '1534440'
        VIDEO_ID = '205047337448'
        channel_page = ChannelPage(self.browser)
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(self.VIDEO_NAME_STUB, description=NEW_DESCRIPTION)
        video_page = VideoPage(self.browser)
        video_page.open(id=VIDEO_ID)
        self.assertion.equal(NEW_DESCRIPTION, video_page.description.text)  # TODO
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(self.VIDEO_NAME_STUB, description=OLD_DESCRIPTION)

class SubscriptionsCase(BaseCase):
    CHANNEL_LINK =  'video/c1100320'
    VIDEO_LINK = 'video/203665445152'

    def test_subscribe_from_channel_page(self):
        channel_page = ChannelPage(self.browser, self.CHANNEL_LINK)
        channel_page.open()
        channel_page.subscribe()
        self.assertTrue(channel_page.is_subscribe() )
        channel_page.unsubscribe()
        self.assertTrue(channel_page.is_not_subscribe() )#TODO

    def test_subscribe_from_video_page(self):
        video_page = VideoPage(self.browser, self.VIDEO_LINK)
        video_page.open()
        video_page.subscribe()
        self.assertTrue(video_page.is_subscribe())
        video_page.unsubscribe()
        self.assertTrue(video_page.is_not_subscribe())  # TODO



