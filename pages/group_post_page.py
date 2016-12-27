# coding=utf-8
from seismograph.ext import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helper import conditions as c


class GroupPostPage(selenium.Page):
    __url_path__ = '/avto.mobile/'

    comment_body = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='topPanelPopup_d'
        )
    )

    comment_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d'
        )
    )

    comment_button = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d_button'
        )
    )

    def get_comments(self):
        return self.browser.find_elements_by_css_selector('div.d_comment_w')

    def open_post_comments(self):
        self.browser.execute_script('''$('.feed_f').find('a').first().click()''')
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.visibility_of(self.comment_body))

    def make_group_comment(self, text):
        self.comment_input.wait()
        self.comment_input.set(text)
        count = len(self.get_comments())
        self.comment_button.wait()
        self.comment_button.click()

        wait = WebDriverWait(self.browser, 10)
        wait.until_not(c.list_len_equals((By.CSS_SELECTOR, 'div.d_comment_w'), count))

        comment = self.get_comments()[-1]
        return comment.text
