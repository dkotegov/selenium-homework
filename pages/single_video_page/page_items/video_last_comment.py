
# -*- coding: utf-8 -*-
from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil
import utils

class Class(selenium.PageItem):
    pass

class LastComment(PageItem):


    __area__ = utils.query('DIV', _class=query.contains('last-comment') )

    IS_DELETED_CLASS = 'delete-stub_info'

    remove  = utils.query('A', _class=query.contains('comments_remove'))
    author  = utils.query('A', _href=query.startswith('/profile') )
    recover = utils.query('A', _class=query.contains('delete-stub_cancel'))
    klass   = utils.query('SPAN', _id=query.contains('hook_VoteHook') )
    content = utils.text_field('DIV', _class=query.contains('comments_text'))

    @property
    def is_deleted(self):
        self.we.wait()
        return len(self.we.find_elements_by_class_name(self.IS_DELETED_CLASS)) > 0

    class Content(PageItem):

        X_TEXT = ".//div[contains(@class,'comments_text')]//span"

        def get_text(self):
            content = self.we.find_element_by_xpath(self.X_TEXT)
            return content.text

    el_content = PageElement(
        query(
            query.DIV,
            _class=query.contains('comments_text')
        ),
        we_class=Content
    )

    el_klass = PageElement(
        query(
            query.SPAN,
            _id=query.contains('hook_VoteHook')
        )
    )

    def switch_klass(self):
        self.el_klass.we.click()

    def is_klassed(self):
        X_PATH = ".//span[contains(text(), 'Вы')]"
        return len(self.we.find_elements_by_xpath(X_PATH)) > 0

    el_reply = PageElement(
        query(
            query.A,
            _class=query.contains('comments_reply')
        )
    )

    def check_attachment(self):
        X_PHOTO = ".//a[contains(@class,'collage_cnt')]"
        photo_lst = self.we.find_elements_by_xpath(X_PHOTO)
        X_VIDEO = ".//a[contains(@class,'video-card_lk')]"
        video_lst = self.we.find_elements_by_xpath(X_VIDEO)
        is_attached = (len(photo_lst) > 0) or (len(video_lst) > 0)
        return is_attached