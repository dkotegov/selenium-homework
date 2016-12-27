# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException


class ProfilePage(selenium.Page):
    __url_path__ = '/profile/572412246941/'

    checked_post = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media-text_cnt_tx textWrap'
        )
    )

    @selenium.polling.wrap(delay=1)
    def wait_deleted_text(self):
        self.browser.execute_script("$('a.al.feed_close').first().click()")
        try:
            return self.browser.find_elements_by_css_selector('span.delete-stub_info.tico')[1].text
        except:
            raise WebDriverException(msg='Timeout at waiting deleted post')

    def get_first_post(self):
        self.checked_post.wait()
        return self.checked_post.text

    def delete_my_post(self):
        return self.wait_deleted_text()
