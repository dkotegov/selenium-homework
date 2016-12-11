# -*- coding: utf-8 -*-
import seismograph

from base_case import BaseCase
from pages.channel_page import ChannelPage
from pages.myvideos_page import MyVideosPage
from pages.video_page import VideoPage

suite = seismograph.Suite(__name__, require=['selenium'])


@suite.register
class CreateChannelCase(BaseCase):
    TEST_CHANNEL1 = 'TEST_CHANNEL1'
    TEST_CHANNEL2 = 'TEST_CHANNEL2'

    def setup(self):
        super(CreateChannelCase, self).setup()
        self.video_page = MyVideosPage(self.browser)
        self.video_page.open()
        self.channel_page = ChannelPage(self.browser)

    def test_create(self):
        self.video_page.create_channel(self.TEST_CHANNEL1)
        self.assertion.is_in(self.TEST_CHANNEL1, self.browser.page_source)  # TODO использовать список каналов
        self.channel_page.delete_channel()
        self.assertion.is_not_in(self.TEST_CHANNEL1, self.browser.page_source)

    def test_create_from_left_menu(self):
        self.video_page.create_channel_left_menu(self.TEST_CHANNEL2)
        self.assertion.is_in(self.TEST_CHANNEL2, self.browser.page_source)
        self.channel_page.delete_channel()
        self.assertion.is_not_in(self.TEST_CHANNEL2, self.browser.page_source)

@suite.register
class AddVideoCase(BaseCase):
    FIRST_CHANNEL_ID = '1533672'
    SECOND_CHANNEL_ID = '1566696'
    VIDEO_URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    VIDEO_TITLE = 'Rick Astley - Never Gonna Give You Up'
    DEFAULT_VIDEOS_COUNT = 0

    def setup(self):
        super(AddVideoCase, self).setup()
        self.channel_page = ChannelPage(self.browser)

    def test_left_button(self):
        self.channel_page.open(id=self.FIRST_CHANNEL_ID)
        self.channel_page.add_video_main(self.VIDEO_URL)

    def test_button_on_channel_page(self):
        self.channel_page.open(id=self.FIRST_CHANNEL_ID)
        self.channel_page.add_video(self.VIDEO_URL)

    def teardown(self):
        self.assertion.is_in(self.VIDEO_TITLE, self.channel_page.get_videos_titles())
        self.assertion.equal(self.channel_page.videos_count, self.DEFAULT_VIDEOS_COUNT + 1)
        self.channel_page.delete_video(self.VIDEO_TITLE)
        self.assertion.is_not_in(self.VIDEO_TITLE, self.channel_page.get_videos_titles())
        self.assertion.equal(self.channel_page.videos_count, self.DEFAULT_VIDEOS_COUNT)
        super(AddVideoCase, self).teardown()



# @suite.register
class ChangeChannelCase(BaseCase):

    def test_move_video(self):
        DESTINATION_ID = '1534952'
        SOURCE_ID = '1535208'
        DESTINATION_NAME ='DESTINATION_CHANNEL'
        SOURCE_NAME = 'SOURCE_CHANNEL'
        VIDEO_NAME = 'VIDEO_TO_MOVE'

        source = ChannelPage(self.browser)
        destination = ChannelPage(self.browser)
        source.open(id=SOURCE_ID)
        source.move_video(VIDEO_NAME, DESTINATION_NAME)
        self.assertion.is_not_in(VIDEO_NAME, source.get_videos_titles())
        destination.open(id=DESTINATION_ID)
        self.assertion.is_in(VIDEO_NAME, destination.get_videos_titles())
        destination.move_video(VIDEO_NAME, SOURCE_NAME)

    def test_rename_channel(self):
        CHANNEL_ID = '1534696'
        CHANNEL_NAME = 'TEST_RENAME'
        NEW_CHANNEL_NAME = 'NEWNAME'

        channel_page = ChannelPage(self.browser)
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_channel(NEW_CHANNEL_NAME)
        self.assertion.equal(channel_page.channel_name, NEW_CHANNEL_NAME)
        channel_page.edit_channel(CHANNEL_NAME)



    def test_add_tags(self):#TODO исправить
        CHANNEL_ID = '1534184'
        NEW_TAG = 'TAGTAGTAG'
        VIDEO_NAME = 'VIDEO_TO_TEST_TAGS'

        channel_page = ChannelPage(self.browser)
        channel_page.open(id = CHANNEL_ID)
        channel_page.edit_video(VIDEO_NAME, new_tags=NEW_TAG)
        self.assertion.is_in(NEW_TAG, channel_page.get_video_tags(VIDEO_NAME))
        channel_page.edit_video(VIDEO_NAME, remove_tags=NEW_TAG)
        self.assertion.is_not_in(NEW_TAG, channel_page.get_video_tags(VIDEO_NAME))

    def test_change_video_name(self):
        CHANNEL_ID = '1533928'
        VIDEO_ID = '202886615528'
        NEW_VIDEO_NAME = 'NEW_VIDEO_NAME'
        OLD_VIDEO_NAME = 'OLD_VIDEO_NAME'

        channel_page = ChannelPage(self.browser )
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(OLD_VIDEO_NAME, title=NEW_VIDEO_NAME)
        video_page = VideoPage(self.browser)
        video_page.open(id=VIDEO_ID)
        video_title = video_page.title.text
        self.assertion.equal(NEW_VIDEO_NAME, video_title)
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(NEW_VIDEO_NAME, title=OLD_VIDEO_NAME)

    def test_change_video_description(self):
        OLD_DESCRIPTION = 'OLD_DESCRIPTION'
        NEW_DESCRIPTION = 'NEW_DESCRIPTION'
        CHANNEL_ID = '1534440'
        VIDEO_ID = '205047337448'
        VIDEO_NAME = 'Rick Astley - Never Gonna Give You Up'

        channel_page = ChannelPage(self.browser)
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(VIDEO_NAME, description=NEW_DESCRIPTION)
        video_page = VideoPage(self.browser)
        video_page.open(id=VIDEO_ID)
        self.assertion.equal(NEW_DESCRIPTION, video_page.description.text)
        channel_page.open(id=CHANNEL_ID)
        channel_page.edit_video(VIDEO_NAME, description=OLD_DESCRIPTION)


@suite.register
class SubscriptionsCase(BaseCase):
    CHANNEL_ID = '1100320'
    VIDEO_ID = '203665445152'
    DEFAULT_SUBSCRIPTIONS_COUNT = 0

    def test_subscribe_from_channel_page(self):
        self.page = ChannelPage(self.browser)
        self.page.open(id = self.CHANNEL_ID)

    def test_subscribe_from_video_page(self):
        self.page = VideoPage(self.browser)
        self.page.open(id=self.VIDEO_ID)

    def teardown(self):
        self.page.subscribe()
        self.assertion.true(self.page.is_subscribe())
        self.assertion.equal(self.page.subscriptions_count, self.DEFAULT_SUBSCRIPTIONS_COUNT + 1)
        self.page.unsubscribe()
        self.assertion.false(self.page.is_subscribe())  # TODO
        self.assertion.equal(self.page.subscriptions_count, self.DEFAULT_SUBSCRIPTIONS_COUNT)
        super(SubscriptionsCase, self).teardown()



