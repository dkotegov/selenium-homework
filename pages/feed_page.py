# coding=utf-8
from seismograph.ext import selenium
from pages.comment_page import CommentPage
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helper import conditions as c


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    post_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='posting-form_itx_w'
        )
    )

    active_tab = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='filter_i __active iblock-cloud_show'
        )
    )

    active_menu = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='sc-menu __reshare __noarrow sc-menu__top'
        )
    )

    @selenium.polling.wrap(delay=1)
    def set_smth(self, element, text):
        element.set(text)

    @selenium.polling.wrap(delay=1)
    def wait_like_change(self, old, idx, script):
        self.browser.execute_script(script)
        text = self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', idx)
        if old == text:
            raise WebDriverException(msg='Timeout at waiting like value changed')
        return text

    @selenium.polling.wrap(delay=1)
    def wait_repost_change(self):
        self.active_menu.wait()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException(msg='Timeout at waiting repost feed')

    @selenium.polling.wrap(delay=1)
    def wait_popular(self):
        self.browser.execute_script('''$('.filter_i')[2].click()''')
        if u'Популярное' not in self.active_tab.text:
            raise WebDriverException(msg='Timeout at waiting Popular tab opened')

    @selenium.polling.wrap(delay=1)
    def show_post(self):
        self.post_input.wait()
        self.post_input.click()
        if not self.browser.current_url.endswith('/post'):
            raise WebDriverException(msg='Timeout at waiting post modal')

    @selenium.polling.wrap(exceptions=[PollingTimeoutExceeded])
    def open_menu_in_feed(self):
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        self.active_menu.wait()

    @selenium.polling.wrap(delay=1)
    def get_elem_text_by_css_and_idx(self, parent, css, idx):
        return parent.find_elements_by_css_selector(css)[idx].text

    @selenium.polling.wrap(delay=1)
    def get_author_title(self):
        return self.browser.find_element_by_xpath(
            '//*[@class="feed"]/div[3]/div[1]/span[1]/span/a').get_attribute('href')

    def get_popular_content(self):
        self.wait_popular()

    def get_author(self):
        self.get_popular_content()
        return self.get_author_title()

    def click_post_title(self):
        self.browser.execute_script('''$('.feed_h').first().find('a').first().click()''')

    def get_own_post_like(self):
        return self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', 0)

    def make_like_on_own_post(self, before):
        return self.wait_like_change(before, 0, '''$('.feed_f').first().find('button')[1].click()''')

    def click_post_comment(self):
        self.browser.execute_script('''$('div.feed_cnt').first().find('a.h-mod.widget_cnt').first().click()''')
        comment_body = CommentPage(self.browser)
        comment_body.wait_popup()

    def make_comment(self, text):
        comment_body = CommentPage(self.browser)
        self.set_smth(comment_body.comment_input, text)
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        return comment_div.text

    def click_status_comment(self):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(self.browser)
        comment_body.wait_popup()

    def make_self_comment(self, text):
        comment_body = CommentPage(self.browser)
        self.set_smth(comment_body.comment_input, text)
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        return comment_div.text

    def make_like_on_self_comment(self, unlike=False):
        comment_body = CommentPage(self.browser)
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        wait = WebDriverWait(self.browser, 10)
        if unlike:
            like_div.click()
            res = u'Класс'
            wait.until(c.text_to_be_present_in_element(like_div, res))
        else:
            res = u'Вы'
            wait.until(c.text_to_be_present_in_element(like_div, res))
        return res

    def make_repost(self):
        self.wait_repost_change()
        return self.active_menu.text

    def get_feed_like(self):
        return self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', -1)

    def make_feed_like(self, before):
        return self.wait_like_change(before, -1, '''$('button.h-mod.widget_cnt.controls-list_lk').last().click()''')

    def get_post(self):
        url = self.browser.current_url
        self.browser.execute_script('''$('.feed_b').first().find('a').first().click()''')
        wait = WebDriverWait(self.browser, 10)
        wait.until_not(c.in_url(url))
        return self.browser.current_url
