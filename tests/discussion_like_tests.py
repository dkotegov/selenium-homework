# -*- coding: utf-8 -*-
"""Test ability to like video."""
import os
import unittest
import time

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects import AuthPage, DiscussionPage


class DiscussionLikeTestCase(unittest.TestCase):

    def setUp(self):
        BROWSER = os.environ.get('BROWSER', 'FIREFOX')

        self.username = os.environ.get('OKRU_USERNAME')
        self.login = os.environ['OKRU_LOGIN']
        self.password = os.environ['OKRU_PASSWORD']

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, BROWSER).copy()
        )
        self.is_logged = self.auth()

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.set_username(self.username)
        auth_form.set_login(self.login)
        auth_form.set_password(self.password)
        auth_form.submit()
        return auth_form.is_logged

    def test_to_like_and_unlike_comment_in_discussion(self):
        if self.is_logged:
            discussion_page = DiscussionPage(self.driver)
            discussion_page.open()

            like_button = discussion_page.like_button_under_comment
            like_button.like()
            like_controller = discussion_page.like_button_under_comment_controller
            has_your_like = like_controller.has_your_like()
            self.assertTrue(has_your_like)

            unlike_button = discussion_page.unlike_button_under_comment
            unlike_button.unlike()
            like_controller = discussion_page.like_button_under_comment_controller
            has_your_like = like_controller.has_your_like()
            self.assertFalse(has_your_like)
        else:
            self.fail('Connection Error: User not logged')

    def test_to_find_yourself_in_liked_users(self):
        if self.is_logged:
            discussion_page = DiscussionPage(self.driver)
            discussion_page.open()

            like_button = discussion_page.like_liked_by_other_users_button_under_comment
            like_button.like()
            list_liked_users = discussion_page.list_liked_users
            has_your_like = list_liked_users.has_your_like(self.username)
            self.assertTrue(has_your_like)

            list_liked_users.close_popup()

            unlike_button = discussion_page.unlike_liked_by_other_users_button_under_comment
            unlike_button.unlike()
            list_liked_users = discussion_page.list_liked_users
            has_your_like = list_liked_users.has_your_like(self.username)
            self.assertFalse(has_your_like)
        else:
            self.fail('Connection Error: User not logged')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
