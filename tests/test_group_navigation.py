# -*- coding: utf-8 -*-

import os

import unittest
# import seismograph
import urlparse
import time

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from test_base import Page
from test_base import Component

from test_auth import AuthPage
from test_auth import AuthForm

class CreationPostTest(#seismograph.Case):

    unittest.TestCase):
    USERLOGIN = 'technopark30'
    USERNAME = u'Евдакия Фёдорова'
    PASSWORD = os.environ.get('PASSWORD', 'testQA1')
    # new_post = NewPost
    group_page = GroupPage

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

        # self.group_page = GroupPage(self.driver)
        # self.group_page.open()
        # self.new_post = self.group_page.creating_post

    def tearDown(self):
        self.driver.quit()

    # def test_simple_post(self):
    #     text = "simple post with simple text"
    #
    #     new_post = self.group_page.creating_post
    #     new_post.set_text(text)
    #     new_post.submit()
    #     last_post = self.group_page.get_last_post
    #     self.assertTrue(last_post.is_last_post_new_post(text))
    #     self.group_page.refresh_page()
    #     last_post.delete()
    #     self.group_page.refresh_page()
    #     self.assertFalse(last_post.is_last_post_new_post(text))
