# -*- coding: utf-8 -*-
"""Test ability to like photo."""
import unittest

from base_test_case import BaseTestCase
from page_objects import PhotoPage


class PhotoLikeTestCase(BaseTestCase):

    def test_to_like_and_unlike_photo_button_under_photo(self):
        if self.is_logged:
            PHOTO_INDEX = 0

            photo_page = PhotoPage(self.driver)
            photo_page.open_photo(PHOTO_INDEX)

            like_button = photo_page.like_button_under_photo
            like_button.like()
            liked_users = photo_page.list_liked_users
            self.assertTrue(liked_users.has_your_like(self.username))

            unlike_button = photo_page.unlike_button_under_photo
            unlike_button.unlike()
            liked_users = photo_page.list_liked_users
            self.assertFalse(liked_users.has_your_like(self.username))
        else:
            self.fail('Connection Error: User not logged')

    def test_to_like_and_unlike_photo_button_in_the_right_photo_corner(self):
        if self.is_logged:
            PHOTO_INDEX = 1

            photo_page = PhotoPage(self.driver)
            photo_page.open_photo(PHOTO_INDEX)

            like_button = photo_page.like_button_right_photo_corner
            like_button.like()
            liked_users = photo_page.list_liked_users
            self.assertTrue(liked_users.has_your_like(self.username))

            unlike_button = photo_page.unlike_button_right_photo_corner
            unlike_button.unlike()
            liked_users = photo_page.list_liked_users
            self.assertFalse(liked_users.has_your_like(self.username))
        else:
            self.fail('Connection Error: User not logged')

    def test_to_like_and_unlike_photo_button_above_not_opened_photo(self):
        if self.is_logged:
            photo_page = PhotoPage(self.driver)
            photo_page.open_album()

            like_button = photo_page.like_button_in_album
            like_button.like()
            liked_users = photo_page.list_liked_users_in_album
            self.assertTrue(liked_users.has_your_like(self.username))

            unlike_button = photo_page.unlike_button_in_album
            unlike_button.unlike()
            liked_users = photo_page.list_liked_users_in_album
            self.assertFalse(liked_users.has_your_like(self.username))
        else:
            self.fail('Connection Error: User not logged')


# def main():
#     unittest.main()


# if __name__ == '__main__':
#     main()
