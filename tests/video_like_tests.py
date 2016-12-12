# -*- coding: utf-8 -*-
"""Test ability to like video."""
import unittest

from base_test_case import BaseTestCase
from page_objects import VideoPage


class VideoLikeTestCase(BaseTestCase):

    def test_like_video_click_under_video_player(self):
        if self.is_logged:
            VIDEO_INDEX = 0

            video_page = VideoPage(self.driver)
            video_page.open_video(VIDEO_INDEX)

            like_button = video_page.like_button_under_player
            like_button.like()

            # liked_users = video_page.list_of_liked_users
            # is_current_user_in_liked_users_popup = liked_users.has_your_like(
            #     self.username
            # )
            # self.assertTrue(is_current_user_in_liked_users_popup)

            # # unlike
            # unlike_button = video_page.unlike_button_under_player
            # unlike_button.unlike()
            # liked_users = video_page.list_of_liked_users
            # is_current_user_in_liked_users_popup = liked_users.has_your_like(
            #     self.username
            # )
            # self.assertFalse(is_current_user_in_liked_users_popup)
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

    # def test_like_video_click_inside_player(self):
    #     if self.is_logged:
    #         video_page = VideoPage(self.driver)
    #         video_page.open()

    #         # like
    #         like_button = video_page.like_button_during_play
    #         like_button.like()
    #         liked_users = video_page.list_of_liked_users
    #         is_current_user_in_liked_users_popup = liked_users.has_your_like(
    #             self.username
    #         )
    #         self.assertTrue(is_current_user_in_liked_users_popup)

    #         short_liked_users = video_page.short_message_about_liked_users
    #         short_liked_users.has_your_like()

    #         # unlike
    #         unlike_button = video_page.unlike_button_under_player
    #         unlike_button.unlike()
    #         liked_users = video_page.list_of_liked_users
    #         is_current_user_in_liked_users_popup = liked_users.has_your_like(
    #             self.username
    #         )
    #         self.assertFalse(is_current_user_in_liked_users_popup)
    #     else:
    #         self.fail('Connection Error: User not logged')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
