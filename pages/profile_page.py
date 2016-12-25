# coding=utf-8
from seismograph.ext import selenium

class ProfilePage(selenium.Page):
    __url_path__ = '/profile/572412246941/statuses'

    checked_post = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media-text_cnt_tx textWrap'
        )
    )

    def check_first_post(self, text):
        self.checked_post.wait()
        assert text in self.checked_post.text

    def delete_my_post(self):
        self.browser.execute_script("$('a.al.feed_close').first().click();")
        # self.browser.implicitly_wait(1)
        element = self.browser.find_elements_by_css_selector('span.delete-stub_info.tico')[1]
        assert u'удалена' in element.text
