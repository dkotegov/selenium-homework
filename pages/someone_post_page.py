# coding=utf-8
from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class PostPage(selenium.Page):
    __url_path__ = '/profile/573666484126/statuses/65858517120414'

    post_text = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='posting_form_text_field'
        )
    )


    def makeRepost(self):
        return 1
