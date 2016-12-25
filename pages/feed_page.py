# coding=utf-8
from seismograph.ext import selenium

from pages.comment_page import CommentPage
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    post = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='feed'
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

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_repost_change(self):
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_popular(self):
        self.browser.execute_script('''$('.filter_i')[2].click()''')
        if u'Популярное' not in self.active_tab.text:
            raise WebDriverException

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_message(self, count, comment_body):
        new_count = len(comment_body.find_elements_by_css_selector('div.d_comment_w'))
        if new_count <= count:
            raise WebDriverException

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_like(self, like_div):
        if u'Вы' not in like_div.text:
            raise WebDriverException

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_unlike(self, like_div):
        if u'Класс' not in like_div.text:
            raise WebDriverException

    @selenium.polling.wrap(timeout=20, delay=1)
    def show_post(self):
        self.post_input.wait()
        self.post_input.click()
        if not self.browser.current_url.endswith('/post'):
            raise WebDriverException

    def get_popular_content(self):
        self.wait_popular()
        return self.post

    def get_author(self, content):
        title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="feed"]/div[3]/div[1]/span[1]/span/a')))[0]
        url = title.get_attribute('href')
        return title, url

    def make_like_on_own_post(self):
        like_button = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[0]
        like_button.click()

    def get_status_likes(self):
        like_button = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[0]
        current_counter = int(like_button.find_elements_by_css_selector('span.widget_count')[0].text)
        return current_counter

    def make_comment(self, content, feed_page):
        self.browser.execute_script('''$('div.feed_cnt').first().find('a.h-mod.widget_cnt').first().click()''')
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        comment_body.comment_input.set(u'hmm...')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        assert comment_div.text == 'hmm...'

    def make_self_comment(self, content, feed_page):
        button = content.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        comment_body.comment_input.set(u'lel')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        assert comment_div.text == 'lel'

    def make_like_on_self_comment(self, feed_page):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        comment_body.comment_input.set(u'lel')
        count = len(comment_body.find_elements_by_css_selector('div.d_comment_w'))
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        self.wait_message(count, comment_body)
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        self.wait_like(like_div)
        assert len(like_div.text) == 2
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')

    def make_double_like(self, feed_page):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        comment_body.comment_input.set(u'lel')
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        self.wait_like(like_div)
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        like_div.click()
        self.wait_unlike(like_div)
        assert len(like_div.text) != 2

    def make_like_for_someone_comment(self, feed_page):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        self.wait_like(like_div)
        assert len(like_div.text) == 2
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')

    @selenium.polling.wrap(timeout=20, delay=1)
    def open_menu_in_feed(self):
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        try:
            self.active_menu.wait(1)
        except:
            raise WebDriverException

    def make_repost(self):
        self.get_popular_content()
        self.open_menu_in_feed()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        self.wait_repost_change()
        return self.active_menu.text

    def make_like_two_likes(self):
        self.get_popular_content()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.h-mod.widget_cnt.controls-list_lk')))[-1]
        val = element.text

        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').last().click()''')
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').last().click()''')

        new_val = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[-1].text

        assert val == new_val

    def make_one_like(self):
        self.get_popular_content()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.h-mod.widget_cnt.controls-list_lk')))[-1]
        val = element.text

        self.browser.execute_script('''$('button.h-mod.widget_cnt.controls-list_lk').last().click()''')

        new_val = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[-1].text

        assert val != new_val

    def make_double_click_repost(self):
        self.get_popular_content()
        self.open_menu_in_feed()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        self.wait_repost_change()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        return self.active_menu.text

    # def click_notes(self):
    #     button = self.browser.find_elements_by_css_selector('a.mctc_navMenuSec')[5]
    #     button.click()
