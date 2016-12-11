# coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains

import utils
from seismograph.ext import selenium

class AttachVideoDialog(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _id='hook_Block_AttachShareVideoContent'
    )

    VIDEO = '(.//a[contains(@class,"attachInput")])[1]'
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

    # el_input = PageElement(
    #     query(
    #         query.DIV,
    #         _class=query.contains('js-comments_add comments_add-ceditable'),
    #         _id=query.contains('field_')
    #     ),
    #     we_class=InputField
    # )

    attach_video_button= utils.query('ANY', _class = selenium.query.contains('ic_videoattach') )
    attach_photo_button = utils.query(
            'ANY',
            _class= selenium.query.contains('ic_okphotoattach')
            #href=selenium.query.startswith('javascript')
    )

    attach_photo_from_pc_button = utils.query('INPUT', _class= selenium.query.contains('h-mod html5-upload-link') )
    photo_dialog = selenium.PageElement(AttachPhotoDialog)
    video_dialog = selenium.PageElement(AttachVideoDialog)

    def attach_video(self):
        utils.js_click(self.browser, self.attach_video_button)
        utils.js_click(self.browser, self.video_dialog.video)
        #self.video_dialog.video.click()


    def attach_photo(self):
        utils.js_click(self.browser, self.attach_photo_button)
        self.photo_dialog.add_photo()
        self.input.click()


    def attach_photo_from_pc(self, path):
        self.attach_photo_from_pc_button.send_keys(path)

    # def set_text(self, text):
    #     self.el_input.set_text(text)
    #
    # def submit(self):
    #     self.el_send_btn.send()

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
    DELETE_LAST_COMMENT_XPATH ='(//a[contains(@class, "fade-on-hover comments_remove")])[last()]'
    RECOVER_LAST_COMMENT_XPATH = '(//a[contains(@class, "delete-stub_cancel")])[last()]'
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
        utils.js_click(
             self.browser,
             utils.wait_xpath(self.browser, self.FULLSCREEN_MODE)
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

    #@property
    #def comments_list(self):

    def reply_last_comment(self, text):
        self.last_comment.reply_click()
        self.send_comment_form.add_comment(text)

    def add_comment(self, text=None, video = None, photo = None, photo_pc = None ):
        self.send_comment_form.add_comment(text, video, photo, photo_pc)

    # def delete_last_comment(self):
    #     utils.js_click(
    #         self.browser,
    #         utils.wait_xpath(self.browser, self.DELETE_LAST_COMMENT_XPATH)
    #     )
    #
    # def recover_last_comment(self):
    #     utils.js_click(
    #         self.browser,
    #         utils.wait_xpath(self.browser, self.RECOVER_LAST_COMMENT_XPATH)
    #     )