# coding=utf-8
from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class RepostPage(selenium.Page):
    __url_path__ = '/feed'

    make_reshar_div = selenium.PageElement(
        XPathQueryObject(
            '//div[@data-l="t,reshare-menu"]//div[@data-l="t,now"]'
        )
    )

    make_reshar_div_text_ok = selenium.PageElement(
        XPathQueryObject(
            '//div[@data-l="t,reshare-menu"]//div[@data-l="t,now"]//span[@class="tico",and contains(li, "Опубликовано!")]'
        )
    )

    def wait_for_repost(self):
        self.make_reshar_div.wait()
        return True

    def make_repost(self):
        self.make_reshar_div.click()
        return True

    def isPublished(self):
        try:
            self.make_reshar_div_text_ok.wait()
            return True
        except:
            return False
