# -*- coding: utf-8 -*-
import seismograph

from base_case import BaseCase
from  pages.video_page import VideoPage
from  pages.profile_page import ProfilePage

suite = seismograph.Suite(__name__, require=['selenium'])

@suite.register
class CommentsCase(BaseCase):

    def setup(self):
        super(CommentsCase, self).setup()
        self.video_page = VideoPage(self.browser)

    def test_add_comment(self):
        VIDEO_ID = '206460097000'
        COMMENT = 'TESTCOMMENT__TESTCOMMENT'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.add_comment(COMMENT)
        last_comment = self.video_page.last_comment

        self.assertion.equal(COMMENT, last_comment.content)

        last_comment.remove()
        self.assertion.true(COMMENT, last_comment.is_deleted)

    def test_recover_comment(self):
        VIDEO_ID = '206459769320'
        COMMENT = 'COMMENT_TO_TEST_RECOVER'

        self.video_page.open(id=VIDEO_ID)

        self.video_page.last_comment.remove()
        self.video_page.last_comment.recover()

        self.browser.refresh()
        self.assertion.false( self.video_page.last_comment.is_deleted)

    def test_go_to_author_page(self):
         VIDEO_ID = '206459441640'
         AUTHOR_NAME = u'Дарина Сорокина'

         self.video_page.open(id=VIDEO_ID)
         last_comment =self.video_page.last_comment
         last_comment.to_author_page()
         profile_page = ProfilePage(self.browser)

         self.browser.refresh()
         self.assertion.equal(profile_page.name.text, AUTHOR_NAME)




