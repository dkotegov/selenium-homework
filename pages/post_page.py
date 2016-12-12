# coding=utf-8
from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class PostPage(selenium.Page):
    __url_path__ = '/post'

    post_text = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='posting_form_text_field'
        )
    )

    post_button = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            type='submit',
            _class='button-pro'
        )
    )

    def create_post(self,text):
        self.post_text.wait()
        self.post_text.set(text)
        self.post_button.wait()
        self.post_button.click()
        time.sleep(3)

    def delete_own_post(self):
        return 1

