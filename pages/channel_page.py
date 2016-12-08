# -*- coding: utf-8 -*-
from urlparse import urlsplit

from seismograph.ext import selenium

import utils
from video_page import VideoPage
from .base import Component

class DeleteVideoDialog(selenium.PageItem):
    submit_button = utils.query('INPUT', value= u'Удалить')

class EditVideoDialog(selenium.PageItem):
    EDIT_SUBMIT_XPATH = '//input[@value="Сохранить"]'
    MOVIE_TITLE_NAME = 'st.vv_movieTitle'
    MOVIE_DESCRIPTION_NAME = 'st.vv_movieDescription'
    CHANNEL_ID_NAME = 'st.vv_albumId'
    TAG_INPUT_CLASS = 'tag_it'
    TAG_XPATH = '//div[contains(@class, "tag")]/span'
    TAG_DELETE_XPATH = '//div[contains(@class, "tag")]/span[text()="{}"]/following-sibling::' \
                       '*/descendant::i[contains(@class,"tag_del")]'

    title_input = utils.query('INPUT', name='st.vv_movieTitle')
    description_input = utils.query('INPUT', name='st.vv_movieDescription')
    tags_input = utils.query('INPUT', _class = 'tag_it')
    channel_select = utils.query('SELECT', name='st.vv_albumId')
    submit_button = utils.query('INPUT', value=u'Сохранить')

    def set_title(self, title):
        title_input = utils.wait_name(self.driver, self.MOVIE_TITLE_NAME)
        utils.replace_text(title_input, title)

    def add_tag(self, tag):
        tags_input = utils.wait_class(self.driver, self.TAG_INPUT_CLASS)
        tags_input.send_keys(tag)

    def delete_tag(self, tag):
        utils.wait_class(self.driver, self.TAG_INPUT_CLASS)
        delete_elem = utils.wait_xpath(self.driver, self.TAG_DELETE_XPATH.format(tag))
        delete_elem.click()
        # self.driver.execute_script('arguments[0].click();', delete_elem)

    @property
    def tag_list(self):
        utils.wait_class(self.driver, self.TAG_INPUT_CLASS)
        return self.driver.find_elements_by_xpath(self.TAG_XPATH)

    def set_description(self, description):
        description_input = utils.wait_name(self.driver, self.MOVIE_DESCRIPTION_NAME)
        utils.replace_text(description_input, description)

    def move(self, new_channel):
        channel_input = utils.wait_name(self.driver, self.CHANNEL_ID_NAME)
        channel_input.send_keys(new_channel)

    def submit(self):
        utils.wait_xpath(self.driver, self.EDIT_SUBMIT_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page


class ChannelPage(selenium.Page):
    __url_path__ = "/video/c{id}"

    DELETE_BUTTON_CLASS = 'vl_ic_delete'
    DELETE_VIDEO_SUBMIT_XPATH = '//input[@value="Удалить"]'
    CHANNEL_NAME_XPATH = '//div[@class="mml_ucard_n_g"]'
    EDIT_BUTTON_CLASS = 'vl_ic_edit'
    ADD_VIDEO_CLASS = 'vl_ic_add-video'
    CONFIRM_DELETE_XPATH = '//input[@value="Удалить"]'
    VIDEOS_LINKS_XPATH = '//div[@class="vid-card js-sortable"]/child::a'  # TODO Исправить
    DELETE_FIRST_VIDEO_XPATH = '//a[@class="vid-card_ac_i ic vl_ic_delete"]'
    # TODO Упростить
    CHANGE_VIDEO_XPATH_TEMPLATE = '//div[@class="vid-card js-sortable"]/child::a[@title="{}"]/following-sibling::' \
                                  'div[@class="vid-card_ac"]/descendant::a[@class="vid-card_ac_i ic vl_ic_{}"]'
    DELETE_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}', 'delete')
    EDIT_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}', 'edit')
    EDIT_FIRST_VIDEO_XPATH = '//a[@class="vid-card_ac_i ic vl_ic_edit"]'
    VIDEO_LINK_CLASS = 'vid-card_img__link'
    VIDEO_LINK_XPATH = '//a[@title="{}"]'
    SUBSCRIBE_XPATH = '//a[starts-with(@id,"vv_btn_album_subscribe")]'
    UNSUBSCRIBE_XPATH = '//a[starts-with(@id,"vv_btn_album_unsubscribe")]'
    IS_SUBSCRIBE_XPATH = '//a[starts-with(@id,"vv_btn_album_subscribe") and @class="vl_btn invisible"]'
    NOT_SUBSCRIBE_XPATH = '//a[@class="vl_btn invisible __unsubscribe"]'

    delete_button = utils.query('SPAN', _class='tico_img vl_ic_delete')  # TODO
    edit_video_buttons = utils.query('A', _class='vid-card_ac_i ic vl_ic_edit')
    channel_name = utils.query('DIV', _class="mml_ucard_n_g")
    delete_video_dialog = selenium.PageElement(DeleteVideoDialog)
    edit_video_dialog = selenium.PageElement(EditVideoDialog)

    # def __init__(self, driver, path):
    #     super(ChannelPage, self).__init__(driver)
    #     self.PATH = path

    def delete_channel(self):
        # utils.wait_class(self.driver, self.DELETE_BUTTON_CLASS).click()
        # confirm_delete = utils.wait_xpath(self.driver, self.CONFIRM_DELETE_XPATH)
        # confirm_delete.click()
        self.delete_button.click()
        self.delete_video_dialog.submit_button.click()
        utils.wait_change_url(self.browser)

    # def channel_name(self):
    #     name_elem = utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH)
    #     return name_elem.text

    def click_edit(self):
        utils.wait_class(self.driver, self.EDIT_BUTTON_CLASS).click()
        return ChangeChannelDialog(self.driver)

    def click_add_video(self):
        utils.wait_class(self.driver, self.ADD_VIDEO_CLASS).click()
        return AddVideoDialog(self.driver)

    def add_video_by_url(self, url):
        add_video_dialog = self.click_add_video()
        add_video_dialog.choose_add_from_internet()
        add_video_dialog.set_url(url)
        page = add_video_dialog.submit()
        page.open()
        return page

    def edit_channel(self, new_name):
        change_channel_dialog = self.click_edit()
        change_channel_dialog.set_channel_name(new_name)
        page = change_channel_dialog.submit()
        page.open()
        return page

    def delete_video_by_name(self, name):  # TODO
        delete_button = utils.wait_xpath(self.driver, self.DELETE_VIDEO_XPATH_TEMPLATE.format(name))
        self.driver.execute_script('arguments[0].click();', delete_button)
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()
        self.wait_clickable()
        return self

    def delete_video(self):
        delete_button = utils.wait_xpath(self.driver, self.DELETE_FIRST_VIDEO_XPATH)
        self.driver.execute_script('arguments[0].click();', delete_button)
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()
        self.wait_clickable()
        return self

    def click_edit_video(self, name):
        edit_button = utils.wait_xpath(self.driver, self.EDIT_VIDEO_XPATH_TEMPLATE.format(name))
        self.driver.execute_script('arguments[0].click();', edit_button)
        return EditVideoDialog(self.driver)

    def edit_video(self, name, title=None, description=None, new_tags=None, remove_tags=None):
        #edit_video_dialog = self.click_edit_video(name)
        self.edit_first_video_button.click()
        if title is not None:
            self.edit_video_dialog.title_input.set(title)
        if description is not None:
            self.edit_video_dialog.title_input.set(description)
        # if new_tags is not None:
        #     edit_video_dialog.add_tag(new_tags)
        # if remove_tags is not None:
        #     edit_video_dialog.delete_tag(remove_tags)
        #page = edit_video_dialog.submit()
        #self.open()
        #return page

    def move_video(self, name, new_channel):
        edit_first = self.edit_video_buttons.first()
        self.browser.execute_script('arguments[0].click();', edit_first._wrapped)
        #edit_first.click()
        self.edit_video_dialog.channel_select.set(new_channel)
        self.edit_video_dialog.submit_button.click()
        self.browser.refresh()

    def get_video_tags(self, video_name):
        edit_video_dialog = self.click_edit_video(video_name)
        result = [tag.text for tag in edit_video_dialog.tag_list]
        edit_video_dialog.submit()
        return result

    def wait_change(self, old_name):
        utils.wait(self.driver, lambda d: self.channel_name() != old_name)

    def get_videos_elements(self):
        return self.browser.find_elements_by_xpath(self.VIDEOS_LINKS_XPATH)

    def subscribe(self):
        utils.wait_xpath(self.driver, self.SUBSCRIBE_XPATH).click()

    def unsubscribe(self):
        utils.wait_xpath(self.driver, self.UNSUBSCRIBE_XPATH).click()

    def is_subscribe(self):
        return len(utils.wait_many_xpath(self.driver, self.IS_SUBSCRIBE_XPATH)) > 0

    def reload(self):
        channel_id = self.browser.current_url.split('/')[-1]
        self.open(id=channel_id)

    def is_not_subscribe(self):
        return len(utils.wait_many_xpath(self.driver, self.NOT_SUBSCRIBE_XPATH)) > 0

    def get_videos_titles(self):
        return [v.get_attribute('title') for v in self.get_videos_elements()]

    def get_videos_links(self):
        return [v.get_attribute('href') for v in self.get_videos_elements()]

    # def open_video(self):
    #    link = utils.wait_class(self.driver, self.VIDEO_LINK_CLASS)
    #
    #    return VideoPage('')

    # def  open_video_by_name(self, name):
    #    link = utils.wait_class(self.driver, self.VIDEO_LINK_XPATH.format(name))



    def open_video_by_link(self, link):
        return VideoPage(link)

    def wait_clickable(self):
        # condition = (By.CLASS_NAME, self.EDIT_BUTTON_CLASS)
        # utils.wait(self.driver, EC.element_to_be_selected(condition) )
        self.open()  # TODO Сделать по-нормальному




class ChangeChannelDialog(Component):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Сохранить"]'

    def set_channel_name(self, name):
        name_elem = utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH)
        # name_elem.clear()
        utils.replace_text(name_elem, name)

    def submit(self):
        utils.wait_xpath(self.driver, self.CHANNEL_SUBMIT_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page


class AddVideoDialog(Component):
    FROM_INTERNET_XPATH = '//span[@data-target="video_uploader_link"]'
    VIDEO_URL_XPATH = '//input[@name="st.vv_ugLink"]'
    ADD_VIDEO_XPATH = '//div[@class="form-actions video_uploader_actions"]/child::button[text()="Добавить"]'

    def choose_add_from_internet(self):
        utils.wait_xpath(self.driver, self.FROM_INTERNET_XPATH).click()

    def set_url(self, url):
        utils.wait_xpath(self.driver, self.VIDEO_URL_XPATH).send_keys(url)

    def submit(self):
        utils.wait_xpath(self.driver, self.ADD_VIDEO_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page



