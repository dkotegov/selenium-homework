# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from utils import custom_move_to_element


# General elements
class PageElement(object):

    def __init__(self, driver):
        self.driver = driver


class AuthForm(PageElement):

    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@class="button-pro form-actions_yes"]'
    LOGGED_USERNAME = '//h1[contains(@class, "mctc_name_tx")]'

    def set_username(self, username):
        self.username = username

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    @property
    def is_logged(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, self.LOGGED_USERNAME), self.username
                )
            )
            return True
        except TimeoutException:
            return False


class LikesController(PageElement):
    """The page element to show visually your like or not if you didn't like it.

    """
    def is_visible_your_like(self):
        pass

    def is_not_visible_your_unlike(self):
        pass


class LikedUsersListPopup(PageElement):
    """The page element to show users who liked item.

    """
    LINK = ''

    def has_your_like(self, login):
        """Check presence your login in liked users.

        Note:
            Your login must be on the top in list of users if you liked it.
            In the other case your login shouldn't be there.

        """
        pass


class LikeButton(PageElement):
    """The page element to like item.

    """
    BUTTON = ''

    def like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        ).click()
        # self.driver.find_element_by_xpath(self.BUTTON).click()


class UnlikeButton(PageElement):
    """The page element to unlike item.

    """
    BUTTON = ''

    def unlike(self):
        self.driver.find_element_by_xpath(self.BUTTON).click()


class LikeVideoButtonUnderPlayer(LikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'
    # BUTTON = '//button[contains(@class, "widget_cnt controls-list_lk")]'


class UnlikeVideoButtonUnderPlayer(UnlikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'
    # BUTTON = '//button[contains(@class, "widget_cnt controls-list_lk")]'


class LikeVideoButtonInPlayerDuringPlay(LikeButton):

    BUTTON = '//a[@class="html5-vpl_ac_i"]'


class LikedUsersListButtonUnderPlayer(LikedUsersListPopup):

    LINK = '//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"]'

    def has_your_like(self, login):
        xpath = '//ul[@class="widget-list"]/descendant::button[last()-1]'
        # custom_move_to_element(self.driver, xpath)

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(xpath)
        ).perform()

        # login = unicode(login, 'utf8')
        # first_liked_user_in_popup = WebDriverWait(self.driver, 30, 0.1).until(
        #     EC.visibility_of_element_located((By.XPATH, self.LINK))
        # )
        # print(first_liked_user_in_popup.text, 'GOOD')
        # return first_liked_user_in_popup.text == login



























# Like controllers
class VideoLikesController(LikesController):
    pass


# Liked users list
class VideoLikedUsersListPopup(VideoLikesController, LikedUsersListPopup):
    pass


class LikeVideoButtonInPlayerEndOfPlay():
    pass



# # -*- coding: utf-8 -*-
# """Page element classes."""


# # General elements
# class PageElement(object):

#     def __init__(self, driver):
#         self.driver = driver


# class AuthForm(PageElement):

#     LOGIN = '//input[@name="st.email"]'
#     PASSWORD = '//input[@name="st.password"]'
#     SUBMIT = '//input[@class="button-pro form-actions_yes"]'

#     def set_login(self, login):
#         self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

#     def set_password(self, password):
#         self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

#     def submit(self):
#         self.driver.find_element_by_xpath(self.SUBMIT).click()


# class LikesController(PageElement):
#     """The page element to show total likes count.

#     Note:
#         This element is located under the item should be liked.

#     """
#     pass


# class LikedUsersListPopup(PageElement):
#     pass


# # Like controllers
# class VideoLikesController(LikesController):
#     pass


# class PhotoLikesController(LikesController):
#     pass


# class DiscussionLikesController(LikesController):
#     pass


# # Liked users list
# class VideoLikedUsersListPopup(VideoLikesController, LikedUsersListPopup):
#     pass


# class PhotoLikedUsersListPopup(PhotoLikesController, LikedUsersListPopup):
#     pass


# class DiscussionLikedUsersListPopup(DiscussionLikesController, LikedUsersListPopup):
#     pass


# # # Video
# # class VideoPlayer(PageElement):
# #     # open video
# #     pass


# class LikeVideoButtonInPlayerEndOfPlay():
#     pass


# class LikeVideoButtonInPlayerDuringPlay():
#     pass


# class LikeVideoButtonUnderPlayer(VideoLikesController):
#     pass


# # Photo
# class PhotoPlayer(PageElement):
#     # open photo
#     pass


# class LikePhotoButtonUnderPhoto(PhotoPlayer, PhotoLikesController):
#     pass


# class LikePhotoButtonUpperRightPhotoCorner(PhotoPlayer, PhotoLikesController):
#     pass


# class RatingPhotoMenu(PhotoPlayer):
#     pass


# class RatingPhotoButton(RatingPhotoMenu):
#     pass
