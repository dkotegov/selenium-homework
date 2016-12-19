# coding=utf-8
from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject

import time


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
        'gift': '.ugrid_i.soh-s.posR',
    }

    gifts_portlet = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='gift-front_cnt'
        )
    )

    def get_portlet_name(self):
        return self.browser.find_element_by_css_selector(self.page_locators['portlet_name'])

    def open_section(self, section_link_locator):
        section_link = self.browser.find_element_by_css_selector(self.page_locators[section_link_locator])
        section_link.click()
        time.sleep(1)

    def get_gifts_block_count(self):
        return len(self.browser.find_elements_by_css_selector(self.page_locators['gift_block']))

    def get_gifts_count(self):
        return len(self.browser.find_elements_by_css_selector(self.page_locators['gift']))

    def scroll_to_page_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
