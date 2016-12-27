# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException


class GroupPostPage(selenium.Page):
    __url_path__ = '/avto.mobile/'

    comment_body = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='topPanelPopup_d'
        )
    )

    comment_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d'
        )
    )

    comment_button = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d_button'
        )
    )

    @selenium.polling.wrap(delay=1)
    def wait_message(self, count):
        comments = self.get_comments()
        new_count = len(comments)
        if new_count <= count:
            raise WebDriverException(msg='Timeout at waiting new message showed in modal')
        return comments[-1]

    @selenium.polling.wrap(delay=1)
    def wait_popup(self):
        if not self.comment_body.is_displayed():
            raise WebDriverException(msg='Timeout at waiting comment modal')

    def get_comments(self):
        return self.browser.find_elements_by_css_selector('div.d_comment_w')

    def open_post_comments(self):
        self.browser.execute_script('''$('.feed_f').find('a').first().click()''')
        self.wait_popup()

    def make_group_comment(self, text):
        self.comment_button.wait()
        self.comment_input.wait()
        self.comment_input.set(text)
        count = len(self.get_comments())
        self.comment_button.click()
        comment = self.wait_message(count)
        return comment.text
