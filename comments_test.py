# -*- coding: utf-8 -*-
import seismograph

from base_case import BaseCase
from  pages.video_page import VideoPage
from  pages.profile_page import ProfilePage
import os

suite = seismograph.Suite(__name__, require=['selenium'])

@suite.register
class CommentsCase(BaseCase):

    def setup(self):
        super(CommentsCase, self).setup()
        self.video_page = VideoPage(self.browser)
    #
    # def test_add_comment(self):
    #     VIDEO_ID = '206460097000'
    #     COMMENT = 'TESTCOMMENT__TESTCOMMENT'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #
    #     self.video_page.add_comment(COMMENT)
    #     last_comment = self.video_page.last_comment
    #
    #     self.assertion.equal(COMMENT, last_comment.content)
    #
    #     last_comment.remove()
    #     self.assertion.true( last_comment.is_deleted)
    #
    # def test_recover_comment(self):
    #     VIDEO_ID = '206459769320'
    #     COMMENT = 'COMMENT_TO_TEST_RECOVER'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #
    #     self.video_page.last_comment.remove()
    #     self.video_page.last_comment.recover()
    #
    #     self.browser.refresh()
    #     self.assertion.false( self.video_page.last_comment.is_deleted)
    #
    # def test_go_to_author_page(self):
    #      VIDEO_ID = '206459441640'
    #      AUTHOR_NAME = u'Дарина Сорокина'
    #
    #      self.video_page.open(id=VIDEO_ID)
    #      last_comment =self.video_page.last_comment
    #      last_comment.to_author_page()
    #      profile_page = ProfilePage(self.browser)
    #
    #      self.browser.refresh()
    #      self.assertion.equal(profile_page.name.text, AUTHOR_NAME)
    #
    # def test_expand_description(self):
    #      VIDEO_ID = '206459441640'
    #
    #      self.video_page.open(id=VIDEO_ID)
    #
    #      self.video_page.description_item.expand.click()
    #
    #      #self.browser.refresh()
    #      self.assertion.true(self.video_page.description_item.check_expanded())
    #
    # def test_reply(self):#TODO
    #     VIDEO_ID = '206458458600'
    #     COMMENT = 'TESTREPLY__TESTREPLY'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #     self.video_page.reply_last_comment(COMMENT)
    #     #self.browser.refresh()
    #     self.video_page.open(id=VIDEO_ID)
    #
    #
    #     self.assertion.equal(COMMENT, self.video_page.last_comment.content)
    #     self.video_page.last_comment.remove()

    # def test_klass(self):
    #     VIDEO_ID = '206924812776'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #
    #     self.video_page.last_comment.switch_class()
    #     self.browser.refresh()
    #     self.assertion.true(self.video_page.last_comment.is_klassed())
    #
    #     self.video_page.last_comment.switch_class()
    #     self.browser.refresh()
    #     self.assertion.false(self.video_page.last_comment.is_klassed())

    def test_photo_attachment(self):
        VIDEO_ID = '207003062760'

        self.video_page.open(id=VIDEO_ID)
        self.video_page.add_comment( photo=True)

        self.browser.refresh()
        self.assertion.true( self.video_page.last_comment.check_photo_attachment())
        self.video_page.last_comment.remove()

    # def test_video_attachment(self):
    #     VIDEO_ID = '207004439016'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #     self.video_page.add_comment(video=True)
    #
    #     self.assertion.true(self.video_page.last_comment.check_video_attachment())
    #     self.video_page.last_comment.remove()



    # def test_photo_attachment_from_pc(self):
    #     VIDEO_ID = '207005094376'
    #
    #     self.video_page.open(id=VIDEO_ID)
    #     self.video_page.add_comment(photo_pc=os.path.abspath('./unnamed.png'))
    #
    #     self.video_page.last_comment.remove()


