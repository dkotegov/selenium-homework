# -*- coding: utf-8 -*-
"""PageObject classes."""
import urlparse

from page_elements import AuthForm, LikeVideoButtonUnderPlayer, \
    LikedUsersListButtonUnderPlayer, UnlikeVideoButtonUnderPlayer


class Page(object):
    """Main `PageObject` class.

    """
    BASE_URL = 'https://ok.ru/'
    PATH = '/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    """Page to auth in `ok.ru`.

    """
    PATH = '/'

    @property
    def auth_form(self):
        return AuthForm(self.driver)


class VideoPage(Page):
    # TODO: add doc
    """
    """
    PATH = '/video/192156796190'

    @property
    def like_button_under_player(self):
        return LikeVideoButtonUnderPlayer(self.driver)

    @property
    def unlike_button_under_player(self):
        return UnlikeVideoButtonUnderPlayer(self.driver)

    @property
    def list_of_liked_users(self):
        return LikedUsersListButtonUnderPlayer(self.driver)


class PhotoPage(Page):
    pass


class DiscussionPage(Page):
    pass
