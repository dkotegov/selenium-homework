# -*- coding: utf-8 -*-

import os

import unittest
# import seismograph
import urlparse
import time

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from test_base import Page
from test_base import Component

from test_auth import AuthPage
from test_auth import AuthForm

class GroupsPage(Page):

    PATH = "/groups"
    CREATE_POST = "//div[@class='input_placeholder']"
    CREATE_GROUP = "//div[@class='create-group']"#"/a[@class='add-stub al add-stub__hor']"

    @property
    def form(self):
        return SearchGroup(self.driver)

    @property
    def scroll_to_bottom(self):
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath(
                    "//*[contains(@class,'stream-items')]/li[contains(@class,'stream-item')]["+str(31)+"]"))
            except:
                break
        try:
            toTopButton = WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_id("scrollToTop")
            )
            return True
        except:
            return False

    @property
    def open_group(self):
        links = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//li[сontains(@class,'it')]")
        )
        group = links[randint(0, len(links)-1)]
        print group

    def create_group(self, name):
        self.driver.find_element_by_xpath(self.CREATE_GROUP).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//a[@class='create-group-dialog_i']")
        )
        self.driver.find_element_by_xpath("//div[@class='create-group-dialog_cnt']").click()
        print("create publci page tapped")
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id('hook_Form_PopLayerCreateAltGroupDialog2Form')
        )
        self.driver.find_element_by_id("field_name").send_keys(name)
        self.driver.find_element_by_id("field_description").send_keys(u'...')
        Select(self.driver.find_element_by_id('field_pageMixedCategory')).select_by_value('subcatVal12005')
        self.driver.find_element_by_id("hook_FormButton_button_create").click()
        print("submit")
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='posting-form_itx_dec itx_w']")
        )
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//span[@class='mctc_name_holder']/h1")
        )
        return self.driver.find_element_by_xpath("//span[@class='mctc_name_holder']/h1").text


    def my_groups(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//a[@class='lp floatRight'")
        )
        self.driver.find_element_by_xpath("//a[@class='lp floatRight'").click()

    def refresh_page(self):
        self.driver.refresh()

class SearchGroup(Component):
    SEARCH_BLOCK = "//input[@id='query_userAltGroupSearch']"
    SUBMIT = "//span[@class='search-input_control search-input_search-ic']"
    SEARCH_RESULT = "//div[@class='ucard-v']/div[@class='caption']/a"
    ADDITIONAL_ACTIONS = 'tico_simb_txt'
    DELETE_BUTTON = "//i[@class='tico_img ic ic_delete']"
    CONFIRM_BUTTON = "//i[@class='tico_img ic ic_delete']"

    def set_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEARCH_BLOCK)
        )
        self.driver.find_element_by_xpath(self.SEARCH_BLOCK).send_keys(text)

    def check_result(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEARCH_RESULT).text
        )
    def search_placeholder(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEARCH_BLOCK)
        )
        return self.driver.find_element_by_xpath(self.SEARCH_BLOCK).get_attribute("placeholder")
    def open_group(self):
        self.driver.find_element_by_xpath(self.SEARCH_RESULT).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//span[@class='mctc_name_holder']/h1")
        )
        return self.driver.find_element_by_xpath("//span[@class='mctc_name_holder']/h1").text
        # self.driver.execute_script("window.scrollTo(0, 200);")

        # elem = WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_elements_by_class_name(self.ADDITIONAL_ACTIONS)
        # )
        # elem[0].click()
        # while True:
        #     try:
        #         delete = WebDriverWait(self.driver, 30, 0.1).until(
        #             lambda d: d.find_element_by_xpath(self.DELETE_BUTTON)
        #         )
        #         self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        #         break
        #     except:
        #         pass
        #
        # confirm = WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_element_by_id(self.CONFIRM_BUTTON)
        # )
        # confirm.click()
        # WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_element_by_id(self.CONFIRM_BUTTON)
        # )




class NavigationGroupTest(#seismograph.Case):

    unittest.TestCase):
    USERLOGIN = 'technopark30'
    USERNAME = u'Евдакия Фёдорова'
    GROUP_NAME = u'Как я открыл selenium и познал...'
    PASSWORD = os.environ.get('PASSWORD', 'testQA1')
    groups_page = GroupsPage


    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERLOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.user_block.get_username()
        self.assertEqual(user_name, self.USERNAME)
        self.groups_page = GroupsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_scroll(self):
        self.groups_page.open()
        scrolled = self.groups_page.scroll_to_bottom
        self.assertEqual(scrolled, True)

    def test_groups_open(self):
        self.groups_page.open()
        search = self.groups_page.form
        placeholder = search.search_placeholder()
        self.assertEqual(placeholder, u'поиск по группам')


    def test_create_group(self):
        self.groups_page.open()
        name = self.groups_page.create_group(self.GROUP_NAME)
        self.assertEqual(name, self.GROUP_NAME)

    def test_search_created_group(self):
        self.groups_page.open()
        search = self.groups_page.form
        search.set_text(u'Как я открыл selenium и познал...')
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id('hook_Block_UserGroupsSearch')
        )
        search_result = search.check_result()
        print(search_result)
        self.assertEqual(search_result, self.GROUP_NAME)

    def test_open_my_group(self):
        self.groups_page.open()
        search = self.groups_page.form
        search.set_text(u'Как я открыл selenium и познал...')
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id('hook_Block_UserGroupsSearch')
        )
        search_result = search.check_result()
        name = search.open_group()
        self.assertEqual(name, self.GROUP_NAME)
