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
