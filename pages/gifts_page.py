# coding=utf-8
from seismograph.ext import selenium
from seismograph.ext.selenium import ActionChains
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded
from seismograph.utils.common import waiting_for
from selenium.common.exceptions import StaleElementReferenceException


class SearchResults(selenium.PageItem):
    __area__ = selenium.query(selenium.query.DIV, _class="gift-front_cnt")


class GiftsPage(selenium.Page):
    __url_path__ = '/gifts'

    page_locators = {
        'portlet_name': '.gift-front_cnt .portlet_h_name_t',
        'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        'author_section_link': 'a.nav-side_i[href="/gifts/authorGifts"]',
        'postcards_section_link': 'a.nav-side_i[href="/gifts/liveGifts"]',
        'love_section_link': 'a.nav-side_i[href="/gifts/searchBased1"]',
        'friend_section_link': 'a.nav-side_i[href="/gifts/searchBased2"]',
        'flower_section_link': 'a.nav-side_i[href="/gifts/searchBased3"]',
        'compliments_section_link': 'a.nav-side_i[href="/gifts/searchBased4"]',
        'music_section_link': 'a.nav-side_i[href="/gifts/music"]',
        'designer_section_link': 'a.nav-side_i[href="/gifts/designer"]',
        'my_section_link': 'a.nav-side_i[href="/gifts/my"]',
        'gift_block': '.ugrid.__xxxl .ugrid_cnt [data-block="GiftsFrontContentRBx"] > div > div',
        'gift': '.ugrid_i.soh-s.posR > div',
        'search_input': 'input#gf-search-input[type=text]',
        'search_submit': 'input.search_btn.button-pro[type=submit]',
        'gift_tooltip': 'div.sc-menu.gift-front_SM:not(.sc-menu__hidden)',
        'add_music': 'div.portlet.__sidebar-gifts > div > a',
        'music_modal': 'div.modal-new_center',
        'music_modal_submit': 'div.modal-new_cnt button[type=submit][action=link]',
        'song': '.track.soh-s.__selectable.__has-price',
        'choosed_song_title': 'div.portlet.__sidebar-gifts.taCenter > div.textWrap div[title]',

    }

    gifts_portlet = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='gift-front_cnt'
        )
    )

    gifts_music_modal = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='modal-new_center'
        )
    )

    gifts_music_gift = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='portlet __sidebar-gifts taCenter'
        )
    )

    _old_capture = None
    _new_capture = None

    def get_portlet_name(self):
        return self.browser.find_element_by_css_selector(self.page_locators['portlet_name'])

    def get_portlet_name_text(self):
        try:
            return self.browser.find_element_by_css_selector(self.page_locators['portlet_name']).text
        except StaleElementReferenceException:
            return None

    def open_section(self, section_link_locator):
        section_link = self.browser.find_element_by_css_selector(self.page_locators[section_link_locator])
        self._old_capture = self.get_portlet_name_text()
        section_link.click()
        waiting_for(
            func=self.wait_for_text_changed,
            timeout=10,
            exc_cls=PollingTimeoutExceeded,
            message="Couldn't wait for text to change",
            delay=0.5
        )

    def open_music_tab(self):
        music_tab_link = self.browser.find_element_by_css_selector(self.page_locators['add_music'])
        music_tab_link.click()
        self.gifts_music_modal.wait()

    def get_first_selectable_song(self):
        return self.browser.find_element_by_css_selector(self.page_locators['song'])

    def get_selected_song_title(self):
        return self.browser.find_element_by_css_selector(self.page_locators['choosed_song_title'])

    def choose_first_song(self):
        first_song = self.browser.find_element_by_css_selector(self.page_locators['song'])
        first_song.click()
        submit_music_modal = self.browser.find_element_by_css_selector(self.page_locators['music_modal_submit'])
        submit_music_modal.click()
        self.gifts_music_gift.wait()

    def wait_for_text_changed(self):
        self._new_capture = self.get_portlet_name_text()
        # print self._new_capture
        return self._old_capture != self._new_capture

    def get_gifts_block_count(self):
        return len(self.browser.find_elements_by_css_selector(self.page_locators['gift_block']))

    def get_gifts_count(self):
        return len(self.browser.find_elements_by_css_selector(self.page_locators['gift']))

    def get_gifts(self):
        return self.browser.find_elements_by_css_selector(self.page_locators['gift'])

    def get_first_gift(self):
        return self.browser.find_element_by_css_selector(self.page_locators['gift'])

    def scroll_to_page_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def search(self, search_query):
        search_input = self.browser.find_element_by_css_selector(self.page_locators['search_input'])
        search_submit = self.browser.find_element_by_css_selector(self.page_locators['search_submit'])
        search_input.clear()
        search_input.send_keys(search_query)
        search_submit.click()
        self.gifts_portlet.wait()

    def true_move_mouse_to_element(self, element):
        action = ActionChains(self.browser)
        action.context_click(element).perform()
        waiting_for(
            func=self.wait_for_tooltip_showed,
            timeout=10,
            exc_cls=PollingTimeoutExceeded,
            message="Couldn't wait for text to change",
            delay=1
        )

    def hack_move_mouse_to_element(self, element):
        self.browser.execute_script("$('.gift_a').eq(0).mouseover()")
        waiting_for(
            func=self.wait_for_tooltip_showed,
            timeout=10,
            exc_cls=PollingTimeoutExceeded,
            message="Couldn't wait for text to change",
            delay=1
        )

    def wait_for_tooltip_showed(self):
        tooltips = self.get_tooltips()
        return len(tooltips) > 0

    def get_tooltips(self):
        return self.browser.find_elements_by_css_selector(self.page_locators['gift_tooltip'])
