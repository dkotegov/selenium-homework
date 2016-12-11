# coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains

import utils
from base import Page
from seismograph.ext import selenium


class VideoPage(selenium.Page):
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
    VIDEO_WINDOW = '//div[@class="html5-vpl_vid"]'
    VIDEO_COVER = '//div[@class="vid-card_cnt_w invisible"]'
    PROGRESS_BAR = '//div[@class="html5-vpl_progress-bar"]'
    FULLSCREEN_MODE = '//div[@class="html5-vpl_fullscreen"]'
    VIDEO = '//div[@class="html5-vpl_vid_display"]'
    # AD_SKIP = 'div[@class="html5-vpl_adv al-hide"]'

    __url_path__ = '/video/{id}'

    title = utils.query("DIV", _class="portlet_h portlet_h__nb textWrap")
    description = utils.query("DIV", _class="media-text_cnt textWrap js-vp-layer-description_tx")
    close_video_button = utils.query("DIV", _class="ic media-layer_close_ico")
    unsubscribe_button = utils.query('SPAN', _class='vp-layer_subscribe-lbl ic_quit-lg')
    subscriptions_count_elem = utils.query('DIV', _class='vp-layer-channel_ac_count')

    @property
    def subscriptions_count(self):
        return int(self.subscriptions_count_elem.text.split(' ')[0])

    def subscribe(self):
        utils.wait_xpath(self.browser, self.SUBSCRIBE_XPATH).click()

    def unsubscribe(self):
        self.browser.execute_script('arguments[0].click();', self.unsubscribe_button._wrapped)

    def is_subscribe(self):
        self.browser.refresh()
        return len(utils.wait_many_xpath(self.browser, self.UNSUBSCRIBE_XPATH)) > 0

    def play_video(self):
        utils.wait_xpath(self.browser, self.PLAY_VIDEO, 5).click()

    def play_next_video(self):
        utils.wait_xpath(self.browser, self.NEXT_VIDEO).click()
        utils.wait_change_url(self.browser)

    def pause_video(self):
        utils.wait_xpath(self.browser, self.PAUSE_VIDEO, 5).click()

    def rewind_video(self, percent):
        progress_bar = utils.wait_xpath(self.browser, self.PROGRESS_BAR)
        action_chains = ActionChains(self.browser)
        action_chains.move_to_element(progress_bar).move_by_offset(percent, 0).click().perform()

    def stop_video(self):
        action_chains = ActionChains(self.browser)
        action_chains.context_click(utils.wait_xpath(self.browser, self.VIDEO_WINDOW)).perform()
        utils.wait_xpath(self.browser, self.STOP_VIDEO, 5).click()

    def close_video(self):
        utils.wait_xpath(self.browser, self.CLOSE_VIDEO).click()

    def open_related_video_in_new_tab(self):
        link = utils.wait_xpath(self.browser, self.RELATED_VIDEO).get_attribute("href")
        self.browser.execute_script("window.open('about:blank', '_blank');")
        self.browser.switch_to_window(self.browser.window_handles[1])
        self.browser.get(link)

    def open_fullscreen(self):
        elem = utils.wait_xpath(self.browser, self.FULLSCREEN_MODE).click()

    def close_fullscreen(self):
        self.browser.execute_script(
            "$(arguments[0]).click();",
            utils.wait_xpath(self.browser, self.FULLSCREEN_MODE)._wrapped
        )

    def get_url_related_video(self):
        url = utils.wait_xpath(self.browser, self.RELATED_VIDEO).get_attribute("href")
        return url.split('?')[0]

    def get_video_play_time(self):
        return float(utils.wait_xpath(self.browser, self.VIDEO_PLAY_TIME).text.replace(':', '.'))

    def get_video_time_remained(self):
        return float(utils.wait_xpath(self.browser, self.VIDEO_TIME_REMAINED).text.replace(':', '.'))

    def get_video_window_size(self):
        return utils.wait_xpath(self.browser, self.VIDEO_WINDOW).size

    def is_cover_visible(self):
        try:
            self.browser.find_element_by_xpath(self.VIDEO_COVER)
            return False
        except Exception:
            return True
