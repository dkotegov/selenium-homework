# -*- coding: utf-8 -*-
"""Test ability to like video."""
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote, Firefox

from page_objects import AuthPage, VideoPage


class VideoLikeTestCase(unittest.TestCase):

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

    def test_video_like_under_player(self):
        if self.is_logged:
            video_page = VideoPage(self.driver)
            video_page.open()

            # like
            like_button = video_page.like_button_under_player
            like_button.like()
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertTrue(is_current_user_in_liked_users_popup)

            # unlike
            unlike_button = video_page.unlike_button_under_player
            unlike_button.unlike()
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertFalse(is_current_user_in_liked_users_popup)
        else:
            self.fail('Connection Error: User not logged')

    # def test_like_under_player_ui(self):
    #     """Test the color of button under the player.

    #     Note:
    #         If user liked item the button should have orange color else
    #         the color is primary.

    #     """
    #     # TODO
    #     pass

    # def test_video_like_click_inside_player_during_play(self):
    #     if self.is_logged:
    #         video_page = VideoPage(self.driver)
    #         video_page.open()

    #         like_button = video_page.like_button_under_player
    #         like_button.like()
    #         liked_users = video_page.list_of_liked_users
    #         is_current_user_in_liked_users_popup = liked_users.has_your_like(
    #             self.username
    #         )
    #         time.sleep(5)
    #     else:
    #         self.fail('Connection Error: User not logged')



def main():
    unittest.main()


if __name__ == '__main__':
    main()
