# coding=utf-8
from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject

import time


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.ANY,
            id='viewImageLinkId'
        )
    )

    photo_link = selenium.PageElement(XPathQueryObject("//a[@class='mctc_navMenuSec'][2]"))

    photo_check = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='hook_Block_UserAlbumStreamBlock',
        )
    )

    def goto_photo(self):
        self.photo_link.click()
        self.photo_check.wait(timeout=3)
        return self.photo_check.exist

