# coding=utf-8
from seismograph.ext import selenium
from selenium.webdriver.support.ui import WebDriverWait
from helper import conditions as c


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
            _class=selenium.query.contains('button-pro')
        )
    )

    invisible_overlay = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='posting-form_overlay invisible'
        )
    )

    @selenium.polling.wrap(delay=1)
    def wait_overlay(self):
        self.invisible_overlay.wait()

    def create_post(self, text):
        self.post_text.wait()
        self.post_button.wait()
        self.post_text.click()
        self.post_text.send_keys(text)
        self.post_button.click()

        wait = WebDriverWait(self.browser, 10)
        wait.until_not(c.in_url(self.__url_path__))
