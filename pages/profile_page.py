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
    def wait_deleted(self):
        try:
            return self.browser.find_elements_by_css_selector('span.delete-stub_info.tico')[1]
        except:
            raise WebDriverException

    def get_first_post(self):
        self.checked_post.wait()
        return self.checked_post.text

    def delete_my_post(self):
        self.browser.execute_script("$('a.al.feed_close').first().click()")
        element = self.wait_deleted()
        return element.text
