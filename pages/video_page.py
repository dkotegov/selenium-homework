# coding=utf-8
import utils
import time
from base import Page, Component
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class VideoPage(Page):
    VIDEO_TITLE_XPATH = '//div[@class="portlet_h portlet_h__nb textWrap"]'
    VIDEO_DESCRIPTION_XPATH = '//div[@class="media-text_cnt textWrap js-vp-layer-description_tx"]'
    SUBSCRIBE_XPATH = '//a[text()="Подписаться"]'
    UNSUBSCRIBE_XPATH = '//span[@class="vp-layer_subscribe-lbl ic_quit-lg"]'
    PLAY_VIDEO = '//div[@class="html5-vpl_panel_play"]'
    PAUSE_VIDEO = '//div[@class="html5-vpl_panel_play __pause"]'
    STOP_VIDEO = '//div[@al-mousedown="stop()"]'
    CLOSE_VIDEO = '//div[@class="ic media-layer_close_ico"]'
    RELATED_VIDEO = '(//a[@class="vp-layer_video js-vp-layer_video"])[1]'
    NEXT_VIDEO = '//div[@class="html5-vpl_next"]'
    VIDEO_PLAY_TIME = '//div[@class="html5-vpl_time"]'
    VIDEO_TIME_REMAINED = '//div[@class="html5-vpl_time __remained"]'
    VIDEO_WINDOW = '//div[@class="vp_video"]'
    VIDEO_COVER = '//div[@class="vid-card_cnt_w invisible"]'
    PROGRESS_BAR = '//div[@class="html5-vpl_progress-bar"]'
    # AD_SKIP = 'div[@class="html5-vpl_adv al-hide"]'

    def __init__(self, driver, path):
        super(VideoPage, self).__init__(driver)
        self.PATH = path

    @property
    def description(self):
        return utils.wait_xpath(self.driver, self.VIDEO_DESCRIPTION_XPATH).text

    @property
    def title(self):
        return utils.wait_xpath(self.driver, self.VIDEO_TITLE_XPATH).text

    def subscribe(self):
        utils.wait_xpath(self.driver, self.SUBSCRIBE_XPATH).click()

    def unsubscribe(self):
        unsubscribe_button = utils.wait_xpath(self.driver, self.UNSUBSCRIBE_XPATH)
        self.driver.execute_script('arguments[0].click();', unsubscribe_button)

    def is_subscribe(self):
        #self.open()
        return len(utils.wait_many_xpath(self.driver, self.UNSUBSCRIBE_XPATH)) > 0

    def is_not_subscribe(self):
        return len(utils.wait_many_xpath(self.driver, self.SUBSCRIBE_XPATH)) > 0

    def play_video(self):
        utils.wait_xpath(self.driver, self.PLAY_VIDEO, 5).click()

    def play_next_video(self):
        utils.wait_xpath(self.driver, self.NEXT_VIDEO).click()
        utils.wait_change_url(self.driver)

    def pause_video(self):
        utils.wait_xpath(self.driver, self.PAUSE_VIDEO, 5).click()

    def rewind_video(self, percent):
        progress_bar = utils.wait_xpath(self.driver, self.PROGRESS_BAR)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(progress_bar).move_by_offset(percent, 0).click().perform()

    def stop_video(self):
        action_chains = ActionChains(self.driver)
        action_chains.context_click(utils.wait_xpath(self.driver, self.VIDEO_WINDOW)).perform()
        utils.wait_xpath(self.driver, self.STOP_VIDEO, 5).click()

    def close_video(self):
        utils.wait_xpath(self.driver, self.CLOSE_VIDEO).click()

    def open_related_video_in_new_tab(self):
        link = utils.wait_xpath(self.driver, self.RELATED_VIDEO).get_attribute("href")
        self.driver.execute_script("window.open('about:blank', '_blank');")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get(link)

    def get_url_related_video(self):
        url = utils.wait_xpath(self.driver, self.RELATED_VIDEO).get_attribute("href")
        return url.split('?')[0]

    def get_video_play_time(self):
        return float(utils.wait_xpath(self.driver, self.VIDEO_PLAY_TIME).text.replace(':', '.'))

    def get_video_time_remained(self):
        return float(utils.wait_xpath(self.driver, self.VIDEO_TIME_REMAINED).text.replace(':', '.'))

    def is_cover_visible(self):
        try:
            self.driver.find_element_by_xpath(self.VIDEO_COVER)
            return False
        except Exception:
            return True
