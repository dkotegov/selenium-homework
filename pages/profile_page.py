# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded


class ProfilePage(selenium.Page):
    __url_path__ = '/profile/572412246941/'

    checked_post = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media-text_cnt_tx textWrap'
        )
    )

    @selenium.polling.wrap(delay=1, exceptions=(IndexError, WebDriverException))
    def wait_deleted_text(self):
        self.browser.execute_script("$('a.al.feed_close').first().click()")
        return self.browser.find_elements_by_css_selector('span.delete-stub_info.tico')[1].text

    @selenium.polling.wrap(timeout=4, delay=0.5)
    def get_first_post_polling(self, text_expected):
        self.checked_post.wait()
        if text_expected not in self.checked_post.text:
            self.browser.refresh()
            raise WebDriverException('Cant get right text')
        return self.checked_post.text

    def get_first_post(self, text_expected):
        try:
            return self.get_first_post_polling(text_expected)
        except PollingTimeoutExceeded:
            return self.checked_post.text

    def delete_my_post(self):
        return self.wait_deleted_text()
