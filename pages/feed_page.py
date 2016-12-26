# coding=utf-8
from seismograph.ext import selenium
from pages.comment_page import CommentPage
from selenium.common.exceptions import WebDriverException


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

    @selenium.polling.wrap(delay=1)
    def click_smth(self, element):
        element.click()

    @selenium.polling.wrap(delay=1)
    def set_smth(self, element, text):
        element.set(text)

    @selenium.polling.wrap(delay=1)
    def wait_repost_change(self):
        self.active_menu.wait()
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def wait_like_change(self, old, idx, script):
        self.browser.execute_script(script)
        text = self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', idx)
        if old == text:
            raise WebDriverException
        return text

    @selenium.polling.wrap(delay=1)
    def wait_popular(self):
        self.browser.execute_script('''$('.filter_i')[2].click()''')
        if u'Популярное' not in self.active_tab.text:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def wait_message(self, count, comment_body):
        new_count = len(comment_body.find_elements_by_css_selector('div.d_comment_w'))
        if new_count <= count:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def wait_like(self, like_div):
        if u'Вы' not in like_div.text:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def wait_unlike(self, like_div):
        if u'Класс' not in like_div.text:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def show_post(self):
        self.post_input.wait()
        self.post_input.click()
        if not self.browser.current_url.endswith('/post'):
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def open_menu_in_feed(self):
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        try:
            self.active_menu.wait()
        except:
            raise WebDriverException

    @selenium.polling.wrap(delay=1)
    def get_elem_text_by_css_and_idx(self, parent, css, idx):
        return parent.find_elements_by_css_selector(css)[idx].text

    @selenium.polling.wrap(delay=1)
    def get_author_title(self):
        return self.browser.find_element_by_xpath('//*[@class="feed"]/div[3]/div[1]/span[1]/span/a').get_attribute('href')

    @selenium.polling.wrap(delay=1)
    def wait_url_changed(self, url):
        if self.browser.current_url == url:
            raise WebDriverException
        return self.browser.current_url

    def get_popular_content(self):
        self.wait_popular()

    def get_author(self):
        self.get_popular_content()
        return self.get_author_title()

    def make_like_on_own_post(self):
        before = self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', 0)
        after = self.wait_like_change(before, 0, '''$('.feed_f').first().find('button')[1].click()''')
        assert before != after

    def get_status_likes(self):
        return self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', 0)

    def make_comment(self):
        self.browser.execute_script('''$('div.feed_cnt').first().find('a.h-mod.widget_cnt').first().click()''')
        comment_body = CommentPage(self.browser)
        comment_body.wait_popup()
        if not comment_body.comment_input.is_displayed():
            return
        self.set_smth(comment_body.comment_input, u'hmm...')
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        assert comment_div.text == 'hmm...'

    def make_self_comment(self):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(self.browser)
        comment_body.wait_popup()
        self.set_smth(comment_body.comment_input, u'lel')
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        assert comment_div.text == 'lel'

    def make_like_on_self_comment(self, feed_page):
        button = self.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.wait_popup()
        self.set_smth(comment_body.comment_input, u'lel')
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
        self.set_smth(comment_body.comment_input, u'lel')
        self.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        self.wait_like(like_div)
        self.browser.execute_script('''$('.klass_w').last().find('a').click()''')
        like_div.click()
        self.wait_unlike(like_div)
        assert len(like_div.text) != 2

    def make_repost(self):
        self.get_popular_content()
        self.open_menu_in_feed()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        self.wait_repost_change()
        return self.active_menu.text

    def make_one_like(self):
        self.get_popular_content()
        val = self.get_elem_text_by_css_and_idx(self.browser, 'button.h-mod.widget_cnt.controls-list_lk', -1)
        new_val = self.wait_like_change(val, -1, '''$('button.h-mod.widget_cnt.controls-list_lk').last().click()''')

        assert val != new_val

    def make_double_click_repost(self):
        self.get_popular_content()
        self.open_menu_in_feed()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        self.wait_repost_change()
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        return self.active_menu.text

    def get_post(self):
        self.get_popular_content()
        url = self.browser.current_url
        self.browser.execute_script('''$('.feed_b').first().find('a').first().click()''')
        url = self.wait_url_changed(url)
        assert "/topic/" in url
