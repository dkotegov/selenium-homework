# -*- coding: utf-8 -*-
"""Test ability to like video."""
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects import AuthPage, PhotoPage


class PhotoLikeTestCase(unittest.TestCase):

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


def main():
    unittest.main()


if __name__ == '__main__':
    main()
