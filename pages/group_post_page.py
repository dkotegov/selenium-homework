# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException


class GroupPage(selenium.Page):
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

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_popup(self):
        if not self.comment_body.is_displayed():
            raise WebDriverException(msg='Timeout at waiting comment modal')

    def open_post_comments(self):
        self.browser.execute_script('''$('.feed_f').find('a').first().click()''')
        self.wait_popup()

    def make_group_comment(self):
        text = 'hmm..'
        self.comment_input.set(text)
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()

        comment = self.browser.find_elements_by_css_selector('div.d_comment_w')[-1]

        assert text in comment.text
