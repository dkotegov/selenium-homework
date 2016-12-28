from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject


class PhotoPage(selenium.Page):
    first_album = selenium.PageElement(XPathQueryObject("//li[@class='ugrid_i'][1]"))
    check_opened_album = selenium.PageElement(XPathQueryObject("//div[@class='photo-panel_info']"))
    new_album_button = selenium.PageElement(XPathQueryObject("//a[@class='portlet_h_ac lp']"))
    new_album_popup = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='mp_mm_cont',
        )
    )
    new_album_name_area = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='field_photoAlbumName',
        )
    )
    new_album_save_button = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='hook_FormButton_button_album_create',
        )
    )
    album_name = selenium.PageElement(XPathQueryObject("//span[@class='photo-h_cnt_t ellip']"))
    first_photo = selenium.PageElement(XPathQueryObject("//a[@class='photo-card_cnt'][1]"))
    close_button = selenium.PageElement(XPathQueryObject("//div[@class='js-photoLayerClose ic photo-layer_close']"))

    def open_first_album(self):
        self.first_album.click()
        self.check_opened_album.wait(timeout=3)
        return self.check_opened_album.exist

    def create_album(self, name):
        self.new_album_button.click()
        self.new_album_popup.wait(timeout=3)
        self.new_album_name_area.set(name)
        self.new_album_save_button.click()
        self.album_name.wait(timeout=3)
        return self.album_name

    def open_first_photo(self):
        self.first_photo.click()
        self.close_button.wait(timeout=3)
        return self.close_button.exist

    def close_photo(self):
        self.close_button.click()
        return self.close_button.is_displayed()
