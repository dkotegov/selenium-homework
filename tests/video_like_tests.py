# -*- coding: utf-8 -*-
"""Test ability to like video."""
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
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertTrue(is_current_user_in_liked_users_popup)

            unlike_button = video_page.unlike_button_under_player
            unlike_button.unlike()
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertFalse(is_current_user_in_liked_users_popup)
        else:
            self.fail('Connection Error: User not logged')

    def test_like_video_click_inside_player(self):
        if self.is_logged:
            VIDEO_INDEX = 1

            video_page = VideoPage(self.driver)
            video_page.open_video(VIDEO_INDEX)

            like_button = video_page.like_button_inside_player
            like_button.like()
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertTrue(is_current_user_in_liked_users_popup)

            unlike_button = video_page.unlike_button_inside_player
            unlike_button.unlike()
            liked_users = video_page.list_of_liked_users
            is_current_user_in_liked_users_popup = liked_users.has_your_like(
                self.username
            )
            self.assertFalse(is_current_user_in_liked_users_popup)
        else:
            self.fail('Connection Error: User not logged')

    def test_inner_text_button_inside_player(self):
        if self.is_logged:
            VIDEO_INDEX = 2

            video_page = VideoPage(self.driver)
            video_page.open_video(VIDEO_INDEX)

            like_button = video_page.like_button_inside_player
            like_button.like()
            button_inner_text = video_page.button_inside_player_likes_controller
            is_current_user_liked = button_inner_text.has_your_like()
            self.assertTrue(is_current_user_liked)

            unlike_button = video_page.unlike_button_inside_player
            unlike_button.unlike()
            button_inner_text = video_page.button_inside_player_likes_controller
            is_current_user_liked = button_inner_text.has_your_like()
            self.assertFalse(is_current_user_liked)
        else:
            self.fail('Connection Error: User not logged')

    def test_highlight_with_color_liked_button(self):
        if self.is_logged:
            VIDEO_INDEX = 3

            video_page = VideoPage(self.driver)
            video_page.open_video(VIDEO_INDEX)

            like_button = video_page.like_button_under_player
            like_button.like()

            close_button = video_page.close_video_button
            close_button.click()

            video_page.open_video(VIDEO_INDEX)
            self.assertTrue(like_button.like_highlighted())
        else:
            self.fail('Connection Error: User not logged')


# def main():
#     import unittest
#     unittest.main()


# if __name__ == '__main__':
#     main()
