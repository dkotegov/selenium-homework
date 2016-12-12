# -*- coding: utf-8 -*-
"""Test ability to like comments in discussion."""
import unittest

from base_test_case import BaseTestCase
from page_objects import DiscussionPage


class DiscussionLikeTestCase(BaseTestCase):

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
