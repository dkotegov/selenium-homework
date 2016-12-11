# coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains

import utils
from base import Page
from seismograph.ext import selenium


class VideoPage(selenium.Page):

    SUBSCRIBE_XPATH = '//a[text()="Подписаться"]'
    VIDEO_PLAY_TIME = '//div[@class="html5-vpl_time"]'
    STOP = '//div[@al-mousedown="stop()"]'
    VIDEO_WINDOW = '//div[@class="html5-vpl_vid"]'

    unsubscribe_xpath = utils.query('SPAN', _class='vp-layer_subscribe-lbl ic_quit-lg')
    play = utils.query('DIV', _class='html5-vpl_panel_play')
    pause = utils.query('DIV', _class='html5-vpl_panel_play __pause')
    close_vid = utils.query('DIV', _class='ic media-layer_close_ico')
    related_vid = utils.query('A', _class='vp-layer_video js-vp-layer_video')
    next_vid = utils.query('DIV', _class='html5-vpl_next')
    video_time_remained = utils.query('DIV', _class='html5-vpl_time __remained')
    video_cover = utils.query('DIV', _class='vid-card_cnt_w invisible')
    progress_bar = utils.query('DIV', _class='html5-vpl_progress-bar')
    widescreen_mode = utils.query('DIV', _class='html5-vpl_widescreen')
    fullscreen_mode = utils.query('DIV', _class='html5-vpl_fullscreen')
    roll_in_vid = utils.query('DIV', _class='ic media-layer_turn_ico')
    get_url = utils.query('A', _class='html5-vpl_ac_i __link')
    url = utils.query('INPUT', _class='html5-vpl_it')

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
        utils.wait_xpath(self.browser, self.subscribe_xpath).click()

    def unsubscribe(self):
        self.browser.execute_script('arguments[0].click();', self.unsubscribe_button._wrapped)

    def is_subscribe(self):
        self.browser.refresh()
        return len(utils.wait_many_xpath(self.browser, self.unsubscribe_xpath)) > 0

    def play_video(self):
        if not self.is_video_playing():
            self.play.click()

    def play_video_during(self, time):
        curr_time = utils.wait_xpath(self.browser, self.VIDEO_PLAY_TIME).text
        curr_time = utils.time_to_int(curr_time)
        result_time = utils.int_to_time(curr_time + time)
        utils.wait_value(self.browser, self.VIDEO_PLAY_TIME, result_time)

    def play_next_video(self):
        elem = self.next_vid
        next_video_url = elem.get_attribute("href")
        elem.click()
        utils.wait_change_url(self.browser)
        return next_video_url

    def pause_video(self):
        self.pause.click()

    def rewind_video(self, percent):
        progress_bar = self.progress_bar
        progress_bar_width = progress_bar.size['width']
        action_chains = ActionChains(self.browser)
        action_chains.move_to_element(progress_bar).move_by_offset((progress_bar_width/100)*(percent-50), 0).click().perform()

    def stop_video(self):
        action_chains = ActionChains(self.browser)
        action_chains.context_click(utils.wait_xpath(self.browser, self.VIDEO_WINDOW)).perform()
        utils.wait_xpath(self.browser, self.STOP).click()

    def close_video(self):
        self.close_vid.click()

    def open_related_video_in_new_tab(self):
        link = self.related_vid.first().get_attribute("href")
        self.browser.execute_script("window.open('about:blank', '_blank');")
        self.browser.switch_to_window(self.browser.window_handles[1])
        self.browser.get(link)

    def open_fullscreen(self):
        self.fullscreen_mode.click()

    def close_fullscreen(self):
        self.browser.execute_script(
            "$(arguments[0]).click();",
             self.fullscreen_mode._wrapped
        )

    def open_widescreen(self):
        self.widescreen_mode.click()
        utils.wait_screen_change(self.browser, self.VIDEO_WINDOW)

    def rollin_video(self):
        self.roll_in_vid.click()
        utils.wait_screen_change(self.browser, self.VIDEO_WINDOW)

    def get_video_url(self):
        self.get_url.click()
        url = self.url.get_attribute("value")
        return url

    def get_url_related_video(self):
        url = self.related_vid.first().get_attribute("href")
        return url.split('?')[0]

    def get_video_play_time(self):
        return float(utils.wait_xpath(self.browser, self.VIDEO_PLAY_TIME).text.replace(':', '.'))

    def get_video_time_remained(self):
        return float(self.video_time_remained.text.replace(':', '.'))

    def get_video_window_size(self):
        return utils.wait_xpath(self.browser, self.VIDEO_WINDOW).size

    def is_cover_visible(self):
        try:
            self.browser.find_element_by_xpath(self.video_cover)
            return False
        except Exception:
            return True

    def is_video_playing(self):
        try:
            self.browser.find_element_by_xpath(self.pause)
            return True
        except Exception:
            return False
