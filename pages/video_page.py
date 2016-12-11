# coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains

import utils
from seismograph.ext import selenium

class AttachVideoDialog(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _id='hook_Block_AttachShareVideoContent'
    )

    VIDEO = '(.//a[contains(@class,"attachInput")])'
    @property
    def video(self):
        return utils.wait_xpath(self.browser, self.VIDEO)
    #video = utils.wait_xpath(self.browser, '(//a[contains(@class,"ttachInput")])[0]')
    #video = utils.query( 'A' ,_class= selenium.query.contains('attachInput') )


class AttachPhotoDialog(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class=selenium.query.contains('modal-new_center')
    )

    photo = utils.query('DIV', _class= selenium.query.contains('photo-crop_cnt selectable-card'))
    add_btn =utils.query('INPUT', _id= selenium.query.contains('hook_FormButton_button_attach'))

    def add_photo(self):
        self.photo.click()
        self.add_btn.click()

class SendCommentForm(selenium.PageItem):
    INPUT_XPATH = '(.//div[contains(@class, "js-comments_add")])[last()]'
    SUBMIT_XPATH = '(.//button[@class="button-pro form-actions_yes"])[last()]'

    _area__ = selenium.query(
        selenium.query.DIV,
        _class=selenium.query.contains('comments_form')
    )

    @property
    def input(self):
        return utils.wait_xpath(self.browser, self.INPUT_XPATH)

    @property
    def submit(self):
        return utils.wait_xpath(self.browser, self.SUBMIT_XPATH)

    def add_comment(self, text=None,video = None, photo = None, photo_pc = None):
        if text:
            utils.js_set_text(self.browser, self.input, text)
        if video:
            self.attach_video()
        if photo:
            self.attach_photo()
        if photo_pc:
            self.attach_photo_from_pc(photo_pc)
        utils.js_click(self.browser, self.submit)

    attach_button = utils.query('DIV', _class = selenium.query.contains('comments_attach_trigger_ic'))
    attach_video_button= utils.query('ANY', _class = selenium.query.contains('ic_videoattach') )
    attach_photo_button = utils.query(
            'ANY',
            _class= selenium.query.contains('ic_okphotoattach')
    )

    attach_photo_from_pc_button = utils.query('INPUT', _class= selenium.query.contains('h-mod html5-upload-link') )
    photo_dialog = selenium.PageElement(AttachPhotoDialog)
    video_dialog = selenium.PageElement(AttachVideoDialog)

    def attach_video(self):
        utils.js_click(self.browser, self.attach_button)
        utils.js_click(self.browser, self.attach_video_button)
        # action_chains = ActionChains(self.browser)
        # action_chains.\
        #     move_to_element(self.attach_button).\
        #     click().\
        #     move_to_element(self.attach_video_button). \
        #     click().\
        #     move_to_element(self.video_dialog.video).\
        #     click().\
        #     perform()
        utils.js_click(self.browser, self.video_dialog.video)


    def attach_photo(self):
        utils.js_click(self.browser, self.attach_photo_button)
        self.photo_dialog.add_photo()
        self.input.click()


    def attach_photo_from_pc(self, path):
        self.attach_photo_from_pc_button.send_keys(path)


class LastComment(selenium.PageItem):


    #__area__ = utils.query('DIV', _class= selenium.query.contains('last-comment') )

    IS_DELETED_CLASS = 'delete-stub_info'
    IS_KLASSED_XPATH = ".//span[contains(text(), 'Вы')]"
    VIDEO_ATTACHED_XPATH = '".//a[contains(@class,"video-card_lk")]'
    PHOTO_ATTACHED_XPATH = './/a[contains(@class,"collage_cnt")]'

    remove_button  = utils.query('A', _class= selenium.query.contains('comments_remove'))
    author  = utils.query('A', _href= selenium.query.startswith('/profile') )
    recover_button = utils.query('A', _class= selenium.query.contains('delete-stub_cancel'))
    klass   = utils.query('SPAN', _id= selenium.query.contains('hook_VoteHook') )
    content = utils.text_field('DIV', _class= selenium.query.contains('comments_text'))
    reply_button = utils.query('A', _class= selenium.query.contains('comments_reply'))

    def is_klassed(self):
        self.we.wait()
        return len(self.we.find_elements_by_xpath(self.IS_KLASSED_XPATH)) > 0

    def switch_class(self):
        utils.js_click(self.browser, self.klass)

    @property
    def is_deleted(self):
        self.we.wait()
        return len(self.we.find_elements_by_class_name(self.IS_DELETED_CLASS)) > 0

    def remove(self):
        utils.js_click(self.browser, self.remove_button)

    def recover(self):
        utils.js_click(self.browser, self.recover_button)

    def to_author_page(self):
        utils.js_click(self.browser, self.author)

    def reply_click(self):
        utils.js_click(self.browser, self.author)

    def check_photo_attachment(self):
        photo_lst = self.we.find_elements_by_xpath(self.PHOTO_ATTACHED_XPATH)
        return len(photo_lst) > 0

    def check_video_attachment(self):
        video_lst = self.we.find_elements_by_xpath(self.VIDEO_ATTACHED_XPATH)
        return len(video_lst) > 0



class DescriptionItem(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='vp-layer-description'
    )
    expand = utils.query('DIV', _class= selenium.query.contains('js-vp-layer-description_more') )

    def check_expanded(self):
        #el_expand = self.browser.span(_class=query.contains(self.css_expand))
        css_cls = self.expand.attr._class
        return 'invisible' in css_cls

class VideoPage(selenium.Page):

    SUBSCRIBE_XPATH = '//a[text()="Подписаться"]'
    UNSUBSCRIBE_XPATH = '//span[@class="vp-layer_subscribe-lbl ic_quit-lg"]'
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
    send_comment_form = selenium.PageElement(SendCommentForm)
    description_item  = selenium.PageElement(DescriptionItem)
    last_comment = selenium.PageElement(
       selenium.query(
           selenium.query.DIV,
           _class= selenium.query.contains('last-comment')
       ),
       we_class =  LastComment
    )

    @property
    def subscriptions_count(self):
        return int(self.subscriptions_count_elem.text.split(' ')[0])

    def subscribe(self):
        utils.wait_xpath(self.browser, self.subscribe_xpath).click()

    def unsubscribe(self):
        self.browser.execute_script('arguments[0].click();', self.unsubscribe_button._wrapped)

    def is_subscribe(self):
        self.browser.refresh()
        return len(utils.wait_many_xpath(self.browser, self.UNSUBSCRIBE_XPATH)) > 0

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
        utils.js_click(
             self.browser,
             utils.wait_xpath(self.browser,  self.fullscreen_mode)
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

    def reply_last_comment(self, text):
        self.last_comment.reply_click()
        self.send_comment_form.add_comment(text)

    def add_comment(self, text=None, video = None, photo = None, photo_pc = None ):
        self.send_comment_form.add_comment(text, video, photo, photo_pc)

    def is_video_playing(self):
        try:
            self.browser.find_element_by_xpath(self.pause)
            return True
        except Exception:
            return False
