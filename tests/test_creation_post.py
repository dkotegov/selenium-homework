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

class GroupPage(Page):

    PATH = "/group/53389738115166"
    CREATE_POST = "//div[@class='input_placeholder']"

    @property
    def creating_post(self):
        self.driver.find_element_by_xpath(self.CREATE_POST).click()
        return NewPost(self.driver)

    @property
    def get_last_post(self):
        return LastPost(self.driver)

    def refresh_page(self):
        self.driver.refresh()


class NewPost(Component):
    TEXT_POST = "//div[@id='posting_form_text_field']"
    SUBMIT = "//input[@value='Поделиться'][@class='button-pro']"
    VISIBLE_BLOCK = "//div[@class='posting-form']/div[@class='posting-form_overlay invisible']"

    MUSIC = "//a[@id='openmusic']"
    MUSIC_BLOCK = "//div[@id='swtch'][@class='posting-form_controls  posting-form_controls__off']"
    MUSIC_SEARCH = "//div[@class='it_w search-input']/label/input[@class='search-input_it it'][@type='text']"
    TRACK = "//div[@class='posting-form_track  m_portal_track']/span[@class='posting-form_track_info_w show-on-hover']" \
                 "/span[@class='posting-form_track_info ellip']"
    BUTTON_ADD_TRACK = "//div[@class='modal-new_center']/div[@class='modal-new_cnt']/div[@class='form-actions __center']" \
                       "/a[@class='button-pro form-actions_yes']"

    ICO_SETTINGS = "//span[@class='tico toggler lp']/i[@class='tico_img ic ic_settings']"
    MENU_SETTINGS = "//div[@class='jcol-l']/div[@class='iblock-cloud_dropdown h-mod __active']"
    NO_COMMENT = "//div[@class='nowrap']/input[@name='st.toggleComments']"


    def set_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.VISIBLE_BLOCK)
        )
        self.driver.find_element_by_xpath(self.TEXT_POST).send_keys(text)

    def set_music(self, search_text):
        self.driver.find_element_by_xpath(self.MUSIC).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MUSIC_BLOCK)
        )
        self.driver.find_element_by_xpath(self.MUSIC_SEARCH).send_keys(search_text)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TRACK)
        )
        self.driver.find_element_by_xpath(self.TRACK).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BUTTON_ADD_TRACK)
        )
        self.driver.find_element_by_xpath(self.BUTTON_ADD_TRACK).click()

    def set_no_comment(self):
        self.driver.find_element_by_xpath(self.ICO_SETTINGS).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MENU_SETTINGS)
        )
        self.driver.find_element_by_xpath(self.NO_COMMENT).click()





    def submit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class LastPost(Component):
    LAST_POST = "//div[@class='groups_post-w __search-enabled'][1]//div[@class='media-text_cnt']//" \
                "div[@class='media-text_cnt_tx textWrap']"
    LAST_POST_A = "//div[@class='groups_post-w __search-enabled'][1]//div[@class='media-text_cnt']/" \
                  "div[@class='media-text_cnt_tx textWrap']/a[@class='media-text_a']"
    FALLING_MENU = "//div[@class='mlr_top_ac']/div[@class='ic12 ic12_arrow-down lp']"
    DELETE_POST = "//span[@class='tico']/i[@class='tico_img ic ic_delete']"

    ICO_X = "//div[@class='media-layer_close']/div[@class='ic media-layer_close_ico']"
    TEXT_POST_DELETED = "//span[@class='delete-stub_info']"

    TRACK_IN_LAST_POST = "//div[@class='groups_post-w __search-enabled'][1]//a[@class='track_song']"

    COMMENT_IN_LAST_POST = "//div[@class='groups_post-w __search-enabled'][1]//a[@class='h-mod widget_cnt']" \
                           "/span[@class='widget_ico ic12 ic12_comment']"
    COMMENT_CLOSED = "//div[@class='disc_simple_input_cont'][@style='display: block;']//" \
                     "input[@class='disc_simple_input disc_simple_input__im']"

    def is_last_post_new_post(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_POST)
        )
        # print self.driver.find_element_by_xpath(self.LAST_POST).text
        # print text
        if self.driver.find_element_by_xpath(self.LAST_POST).text == text:
            return True
        else:
            return False

    def is_last_post_has_track(self, track):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_POST)
        )
        if self.driver.find_element_by_xpath(self.TRACK_IN_LAST_POST).text == track:
            return True
        else:
            return False

    def is_last_post_without_comments(self):
        text_lock = u"Комментарии к этой теме закрыты администрацией"
        self.driver.find_element_by_xpath(self.COMMENT_IN_LAST_POST).click()
        self.driver.find_element_by_xpath(self.COMMENT_IN_LAST_POST).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENT_CLOSED)
        )
        return self.driver.find_element_by_xpath(self.COMMENT_CLOSED).get_attribute('value') == text_lock

    def delete(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_POST_A)
        )
        self.driver.find_element_by_xpath(self.LAST_POST).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FALLING_MENU)
        )
        self.driver.find_element_by_xpath(self.FALLING_MENU).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_POST)
        )
        self.driver.find_element_by_xpath(self.DELETE_POST).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT_POST_DELETED)
        )
        self.driver.find_element_by_xpath(self.ICO_X).click()


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

        self.group_page = GroupPage(self.driver)
        self.group_page.open()
        self.new_post = self.group_page.creating_post

    def tearDown(self):
        self.driver.quit()

    def test_simple_post(self):
        text = u"simple post with simple text"

        new_post = self.group_page.creating_post
        new_post.set_text(text)
        new_post.submit()
        last_post = self.group_page.get_last_post
        self.assertTrue(last_post.is_last_post_new_post(text))
        self.group_page.refresh_page()
        last_post.delete()
        self.group_page.refresh_page()
        self.assertFalse(last_post.is_last_post_new_post(text))

    def test_post_with_music(self):
        text = u"This is post with music"
        search_text = u"Лабутены"

        new_post = self.group_page.creating_post
        new_post.set_text(text)
        new_post.set_music(search_text)
        new_post.submit()

        last_post = self.group_page.get_last_post
        self.assertTrue(last_post.is_last_post_new_post(text + u'\n#музыка'))
        self.assertTrue(last_post.is_last_post_has_track(search_text))
        self.group_page.refresh_page()
        last_post.delete()
        self.group_page.refresh_page()
        self.assertFalse(last_post.is_last_post_new_post(text))

    def test_post_without_comments(self):
        text = u"This is post without comments"

        new_post = self.group_page.creating_post
        new_post.set_text(text)
        new_post.set_no_comment()
        new_post.submit()

        last_post = self.group_page.get_last_post
        self.assertTrue(last_post.is_last_post_new_post(text))
        self.assertTrue(last_post.is_last_post_without_comments())
        # last_post.is_last_post_without_comments()

        self.group_page.refresh_page()
        last_post.delete()
        self.group_page.refresh_page()
        self.assertFalse(last_post.is_last_post_new_post(text))
