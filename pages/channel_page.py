# -*- coding: utf-8 -*-

from seismograph.ext import selenium

import utils


class DeleteVideoDialog(selenium.PageItem):
    submit_button = utils.query('INPUT', value=u'Удалить')


class EditChannelDialog(selenium.PageItem):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Сохранить"]'

    channel_name_input = utils.query('INPUT', name='st.vv_albumName')
    submit_button = utils.query('INPUT', value=u'Сохранить')

    def set_channel_name(self, name):
        utils.replace_text(self.channel_name_input, name)
        self.submit_button.click()


class EditVideoDialog(selenium.PageItem):
    TAG_XPATH = '//div[contains(@class, "tag")]/span'
    TAG_DELETE_XPATH = '//div[contains(@class, "tag")]/span[text()="{}"]/following-sibling::' \
                       '*/descendant::i[contains(@class,"tag_del")]'

    title_input = utils.query('INPUT', name='st.vv_movieTitle')
    description_input = utils.query('TEXTAREA', name='st.vv_movieDescription')
    tags_input = utils.query('INPUT', _class='tag_it')
    channel_select = utils.query('SELECT', name='st.vv_albumId')
    submit_button = utils.query('INPUT', value=u'Сохранить')

    def add_tag(self, tag):
        self.tags_input.set(tag)

    def delete_tag(self, tag):
        self.tags_input.wait()
        delete_elem = utils.wait_xpath(self.browser, self.TAG_DELETE_XPATH.format(tag))
        self.browser.execute_script('arguments[0].click();', delete_elem._wrapped)

    @property
    def tag_list(self):
        self.tags_input.wait()
        return self.browser.find_elements_by_xpath(self.TAG_XPATH)


class AddVideoDialog(selenium.PageItem):
    ADD_VIDEO_XPATH = '//div[@class="form-actions video_uploader_actions"]/child::button[text()="Добавить"]'

    add_from_internet = utils.query('SPAN', data_target="video_uploader_link")
    url_input = utils.query('INPUT', name='st.vv_ugLink')

    def add_video_by_url(self, url):
        self.add_from_internet.click()
        self.url_input.set(url)
        utils.wait_xpath(self.browser, self.ADD_VIDEO_XPATH).click()


class Counters(selenium.PageItem):
    SUBSCRPTIONS_COUNT_XPATH = '//div[@class="jcol-l"]/descendant::i[contains(@class,"mml_ic_friends")]/..'
    VIDEOS_COUNT_XPATH = '//div[@class="jcol-l"]/descendant::i[contains(@class,"vl_ic_channel")]/..'

    def get_counter_value(self, counter_string):
        return int(counter_string.split(' ')[0])

    @property
    def subscriptions_count(self):
        count_elem = self.browser.find_elements_by_xpath(self.SUBSCRPTIONS_COUNT_XPATH)
        if count_elem:
            counter_string = count_elem[0].text
            return self.get_counter_value(counter_string)
        else:
            return 0

    @property
    def videos_count(self):
        counter_string = utils.wait_xpath(self.browser, self.VIDEOS_COUNT_XPATH).text
        return self.get_counter_value(counter_string)


class ChannelPage(selenium.Page):
    __url_path__ = "/video/c{id}"

    VIDEOS_LINKS_XPATH = '//div[@class="vid-card js-sortable"]/child::a'
    # TODO Упростить
    CHANGE_VIDEO_XPATH_TEMPLATE = '//div[@class="vid-card js-sortable"]/child::a[@title="{}"]/following-sibling::' \
                                  'div[@class="vid-card_ac"]/descendant::a[contains(@class,"vl_ic_{}")]'
    DELETE_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}', 'delete')
    EDIT_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}', 'edit')
    VIDEO_LINK_CLASS = 'vid-card_img__link'
    VIDEO_LINK_XPATH = '//a[@title="{}"]'
    IS_SUBSCRIBE_XPATH = '//a[starts-with(@id,"vv_btn_album_subscribe") and @class="vl_btn invisible"]'

    delete_button = utils.query('SPAN', _class='tico_img vl_ic_delete')  # TODO
    edit_video_buttons = utils.query('A', _class='vid-card_ac_i ic vl_ic_edit')
    channel_name = utils.query('DIV', _class="mml_ucard_n_g")
    edit_channel_button = utils.query('SPAN', _class=selenium.query.contains('vl_ic_edit'))
    subscribe_button = utils.query('A', _id=selenium.query.startswith("vv_btn_album_subscribe"))
    unsubscribe_button = utils.query('A', _id=selenium.query.startswith("vv_btn_album_unsubscribe"))
    add_video_button = utils.query('SPAN', _class=selenium.query.contains('vl_ic_add-video'))
    main_add_video_button = utils.query('DIV', _class='vl_add-video')

    delete_dialog = selenium.PageElement(DeleteVideoDialog)
    edit_channel_dialog = selenium.PageElement(EditChannelDialog)
    edit_video_dialog = selenium.PageElement(EditVideoDialog)
    add_video_dialog = selenium.PageElement(AddVideoDialog)
    counters = selenium.PageElement(Counters)

    def delete_channel(self):
        self.delete_button.click()
        self.delete_dialog.submit_button.click()
        utils.wait_change_url(self.browser)

    @property
    def videos_count(self):
        return self.counters.videos_count

    @property
    def subscriptions_count(self):
        return self.counters.subscriptions_count

    def click_add_video(self):
        utils.wait_class(self.browser, self.ADD_VIDEO_CLASS).click()
        return AddVideoDialog(self.browser)

    def add_video(self, url):
        self.add_video_button.click()
        self.add_video_dialog.add_video_by_url(url)
        self.browser.refresh()

    def add_video_main(self, url):
        self.add_video_button.click()
        self.add_video_dialog.add_video_by_url(url)
        self.browser.refresh()

    def edit_channel(self, new_name):
        self.edit_channel_button.click()
        self.edit_channel_dialog.set_channel_name(new_name)
        self.browser.refresh()

    def delete_video(self, name):
        delete_button = utils.wait_xpath(self.browser, self.DELETE_VIDEO_XPATH_TEMPLATE.format(name))
        self.browser.execute_script('arguments[0].click();', delete_button._wrapped)
        self.delete_dialog.submit_button.click()
        self.browser.refresh()

    def click_edit_video(self, name):
        edit_button = utils.wait_xpath(self.browser, self.EDIT_VIDEO_XPATH_TEMPLATE.format(name))
        self.browser.execute_script('arguments[0].click();', edit_button._wrapped)

    def edit_video(self, name, title=None, description=None, new_tags=None, remove_tags=None):
        self.click_edit_video(name)
        if title is not None:
            utils.replace_text(self.edit_video_dialog.title_input, title)
        if description is not None:
            utils.replace_text(self.edit_video_dialog.description_input, description)
        if new_tags is not None:
            self.edit_video_dialog.add_tag(new_tags)
        if remove_tags is not None:
            self.edit_video_dialog.delete_tag(remove_tags)
        self.edit_video_dialog.submit_button.click()
        self.browser.refresh()

    def move_video(self, name, new_channel):
        self.click_edit_video(name)
        self.edit_video_dialog.channel_select.set(new_channel)
        self.edit_video_dialog.submit_button.click()
        self.browser.refresh()

    def get_video_tags(self, video_name):
        self.click_edit_video(video_name)
        result = [tag.text for tag in self.edit_video_dialog.tag_list]
        self.edit_video_dialog.submit_button.click()
        return result

    def get_videos_elements(self):
        return self.browser.find_elements_by_xpath(self.VIDEOS_LINKS_XPATH)

    def subscribe(self):
        self.browser.execute_script('arguments[0].click();', self.subscribe_button._wrapped)

    def unsubscribe(self):
        self.unsubscribe_button.click()

    def open_video_by_id(self, video_id):
        link = self.browser.div(data_id=video_id)
        link.click()
        utils.wait_change_url(self.browser)

    def is_subscribe(self):
        self.browser.refresh()
        return len(self.browser.find_elements_by_xpath(self.IS_SUBSCRIBE_XPATH)) > 0

    def get_videos_titles(self):
        return [v.get_attribute('title') for v in self.get_videos_elements()]

    def get_videos_links(self):
        return [v.get_attribute('href') for v in self.get_videos_elements()]
