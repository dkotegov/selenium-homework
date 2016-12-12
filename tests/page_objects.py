# -*- coding: utf-8 -*-
"""PageObject classes."""
import urlparse

from page_elements import AuthForm, LikeVideoButtonUnderPlayer, \
    LikedUsersListButtonUnderPlayer, UnlikeVideoButtonUnderPlayer, \
    LikeVideoButtonInPlayerDuringPlay, LikedUsersShortMessageInPlayer, \
    UnlikeVideoButtonInPlayerDuringPlay

from discussion_page_elements import OpenDiscussionLinksChain, \
    LikeCommentInDisscussion, UnlikeCommentInDisscussion, \
    DiscussionCommentLikesController, DiscussionCommentLikedUsers, \
    LikeLikedByOtherUsersCommentInDisscussion, UnlikeLikedByOtherUsersCommentInDisscussion


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
        # self.driver.maximize_window()


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
    def like_button_during_play(self):
        return LikeVideoButtonInPlayerDuringPlay(self.driver)

    @property
    def unlike_button_during_play(self):
        return UnlikeVideoButtonInPlayerDuringPlay(self.driver)

    @property
    def list_of_liked_users(self):
        return LikedUsersListButtonUnderPlayer(self.driver)

    @property
    def short_message_about_liked_users(self):
        return LikedUsersShortMessageInPlayer(self.driver)


class PhotoPage(Page):
    pass






class DiscussionPage(Page):

    def open(self):
        super(DiscussionPage, self).open()
        self.links_to_discussion_chat.open()

    @property
    def links_to_discussion_chat(self):
        return OpenDiscussionLinksChain(self.driver)

    @property
    def like_button_under_comment(self):
        return LikeCommentInDisscussion(self.driver)

    @property
    def unlike_button_under_comment(self):
        return UnlikeCommentInDisscussion(self.driver)

    @property
    def like_button_under_comment_controller(self):
        return DiscussionCommentLikesController(self.driver)

    @property
    def list_liked_users(self):
        return DiscussionCommentLikedUsers(self.driver)

    @property
    def like_liked_by_other_users_button_under_comment(self):
        return LikeLikedByOtherUsersCommentInDisscussion(self.driver)

    @property
    def unlike_liked_by_other_users_button_under_comment(self):
        return UnlikeLikedByOtherUsersCommentInDisscussion(self.driver)