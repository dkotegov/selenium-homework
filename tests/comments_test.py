# -*- coding: utf-8 -*-
import os

import seismograph

from  pages.profile_page import ProfilePage
from  pages.video_page import VideoPage
from tests.base_case import BaseCase

suite = seismograph.Suite(__name__, require=['selenium'])


@suite.register
class CommonCommentsCase(BaseCase):
    def setup(self):
        super(CommonCommentsCase, self).setup()
        self.video_page = VideoPage(self.browser)

    def test_recover_comment(self):
        VIDEO_ID = '206459769320'
        COMMENT = 'COMMENT_TO_TEST_RECOVER'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.last_comment.remove()
        self.video_page.last_comment.recover()

        self.browser.refresh()
        self.assertion.equal(self.video_page.last_comment.content, COMMENT)

    def test_go_to_author_page(self):
        VIDEO_ID = '206459441640'
        AUTHOR_NAME = u'Дарина Сорокина'

        self.video_page.open(id=VIDEO_ID)
        last_comment = self.video_page.last_comment
        last_comment.to_author_page()
        profile_page = ProfilePage(self.browser)

        self.browser.refresh()
        self.assertion.equal(profile_page.name.text, AUTHOR_NAME)

    def test_expand_description(self):
        VIDEO_ID = '206459441640'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.description_item.expand.click()

        self.assertion.true(self.video_page.description_item.check_expanded())

    def test_klass(self):
        VIDEO_ID = '206924812776'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.last_comment.switch_class()
        self.browser.refresh()
        self.assertion.true(self.video_page.last_comment.is_klassed())

        self.video_page.last_comment.switch_class()
        self.browser.refresh()
        self.assertion.false(self.video_page.last_comment.is_klassed())


@suite.register
class AddCommentCase(BaseCase):
    def setup(self):
        super(AddCommentCase, self).setup()
        self.video_page = VideoPage(self.browser)

    def test_photo_attachment(self):
        VIDEO_ID = '207003062760'

        self.video_page.open(id=VIDEO_ID)
        self.video_page.add_comment(photo=True)

        self.browser.refresh()
        self.assertion.true(self.video_page.last_comment.check_photo_attachment())

    def test_video_attachment(self):
        VIDEO_ID = '207004439016'

        self.video_page.open(id=VIDEO_ID)
        self.video_page.add_comment(video=True)

        self.browser.refresh()
        self.assertion.true(self.video_page.last_comment.check_video_attachment())

    def test_photo_attachment_from_pc(self):
        VIDEO_ID = '207005094376'
        IMG_PATH = '../unnamed.png'

        self.video_page.open(id=VIDEO_ID)
        self.video_page.add_comment(photo_pc=os.path.abspath(IMG_PATH))

        self.browser.refresh()
        self.assertion.true(self.video_page.last_comment.check_photo_attachment())

    def test_reply(self):
        VIDEO_ID = '206458458600'
        COMMENT = 'TESTREPLY__TESTREPLY'

        self.video_page.open(id=VIDEO_ID)
        self.video_page.reply_last_comment(COMMENT)
        self.browser.refresh()

        self.assertion.equal(COMMENT, self.video_page.last_comment.content)

    def test_add_comment(self):
        VIDEO_ID = '206460097000'
        COMMENT = 'TESTCOMMENT__TESTCOMMENT'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.add_comment(COMMENT)
        self.browser.refresh()

        last_comment = self.video_page.last_comment
        self.assertion.equal(COMMENT, last_comment.content)

    def teardown(self):
        self.video_page.last_comment.remove()
        self.assertion.true(self.video_page.last_comment.is_deleted)
        super(AddCommentCase, self).teardown()
