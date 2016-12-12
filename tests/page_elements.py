# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from utils import custom_move_to_element


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
    def has_your_like(self):
        pass


class LikedUsersListPopup(PageElement):
    """The page element to show users who liked item.

    """
    LINK_XPATH = '//div[contains(@class, "photo-layer_bottom_block __actions")]//descendant::li[last()]/descendant::button'
    USERNAME_LINK = '(//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"])[1]'

    def has_your_like(self, username):
        """Check presence your `username` in liked users.

        Note:
            Your login must be on the top in list of users if you liked it.
            In the other case your login shouldn't be there.

        """
        username = unicode(username, 'utf8')
        custom_move_to_element(
            self.driver, self.LINK_XPATH, click_times=2
        )

        first_user = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_LINK))
        )
        return first_user.text == username


class LikeButton(PageElement):
    """The page element to like item.

    """
    BUTTON = ''

    def like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        ).click()


class UnlikeButton(PageElement):
    """The page element to unlike item.

    """
    BUTTON = ''

    def unlike(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        ).click()



















class LikedUsersShortMessage(PageElement):
    """The page element to show  message kind of `Вы и 99+` users liked it.

    """
    def has_your_like(self):
        # TODO: internationalization
        """Check presence `Вы` in message after you liked it.

        """
        pass





class LikeVideoButtonUnderPlayer(LikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'


class UnlikeVideoButtonUnderPlayer(UnlikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'


class LikeVideoButtonInPlayerDuringPlay(LikeButton):

    BUTTON = 'html5-vpl_ac_i'

    def like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.BUTTON))
        )
        self.driver.execute_script('$(".%s")[0].click()' % self.BUTTON)


class UnlikeVideoButtonInPlayerDuringPlay(UnlikeButton):

    BUTTON = 'html5-vpl_ac_i'

    def unlike(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.BUTTON))
        )
        self.driver.execute_script('$(".%s")[0].click()' % self.BUTTON)


class LikedUsersListButtonUnderPlayer(LikedUsersListPopup):

    LINK = '//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"]'

    def has_your_like(self, login):
        xpath = '//ul[@class="widget-list"]/descendant::button[last()]'
        custom_move_to_element(self.driver, xpath)

        login = unicode(login, 'utf8')
        first_liked_user_in_popup = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.LINK))
        )
        return first_liked_user_in_popup.text == login


# TODO
class LikedUsersShortMessageInPlayer(LikedUsersShortMessage):

    # LINK = 'a div.html5-vpl_ac_txt'

    # def has_your_like(self):
    #     print('WAIT SHORT')
    #     WebDriverWait(self.driver, 30, 0.1).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, self.LINK))
    #     )
    #     message = self.driver.execute_script('$("a div.html5-vpl_ac_txt")[0].innerText')
    #     print(message, 'RTTTT')

    LINK = 'html5-vpl_ac_txt'

    def has_your_like(self):
        print('WAIT SHORT')
        m = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.LINK))
        )
        message = self.driver.execute_script('$(".html5-vpl_ac_txt")[0].innerText')
        print(message, 'RTTTT')













# Discussion
class OpenDiscussionLinksChain(PageElement):

    OPEN_ALL_DISCUSSIONS = '//li[contains(@class, "toolbar_nav_i")][2]'
    OPEN_MY_DISCUSSIONS = '//div[@id="d-f-tab-fM"]'
    OPEN_DISCUSSION = '//div[contains(@id, "d-item-MOVIE-")][1]'

    def open(self):
        discussions_list = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_ALL_DISCUSSIONS))
        )
        discussions_list.click()

        my_discussions_list = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_MY_DISCUSSIONS))
        )
        my_discussions_list.click()

        discussion_chat = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_DISCUSSION))
        )
        discussion_chat.click()


class LikeCommentInDisscussion(LikeButton):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def like(self):
        # wait for By.CSS_SELECTOR and BUTTON throughs error and so I've decided to
        # wait for BUTTON_WRAPPER
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        self.driver.execute_script('$("%s").click()' % self.BUTTON)


class UnlikeCommentInDisscussion(UnlikeButton):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def unlike(self):
        # wait for By.CSS_SELECTOR and BUTTON didn't work and so I've decided to
        # wait for BUTTON_WRAPPER
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        self.driver.execute_script('$("%s").click()' % self.BUTTON)


class DiscussionCommentLikesController(LikesController):
    """If you liked item you will get `Вы` else `Класс`

    """
    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def has_your_like(self, ):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        like_label = self.driver.execute_script('return $("%s")[0].textContent' % self.BUTTON)
        return like_label == u'Вы'





























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
