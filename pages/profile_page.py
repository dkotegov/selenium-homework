# coding=utf-8
from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class ProfilePage(selenium.Page):
    __url_path__ = '/profile/572412246941'



    def check_first_post(self,text):
        try:
            checked_post = selenium.PageElement(
            XPathQueryObject(
            '//div[contains(text(), "{}")]'.format(text)
            )
            )
            return True
        except:
            return False

    def delete_my_post(self):
        self.browser.execute_script("$('a.al.feed_close')[0].click();")
        time.sleep(1)
        try:
            self.browser.find_elements_by_css_selector('div.feed-list')[0].find_elements_by_css_selector('span.delete-stub_info.tico')[0]
            return True
        except:
            return False
