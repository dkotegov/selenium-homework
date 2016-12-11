# coding=utf-8
from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject

import time


class GiftsPage(selenium.Page):
    __url_path__ = '/gifts'

    page_locators = {
        'portlet_name': '.gift-front_cnt .portlet_h_name_t',
        'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'author_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
        # 'actual_section_link': 'a.nav-side_i[href="/gifts"]',
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
