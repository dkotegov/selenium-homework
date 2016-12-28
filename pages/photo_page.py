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
    photo = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='__plpcte_target',
        )
    )
    next_arrow = selenium.PageElement(XPathQueryObject("//span[@class='arw_ic']"))
    rotate_link = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='rotation-link-layer'
        )
    )

    image_0deg = selenium.PageElement(XPathQueryObject("//img[@class='photo-layer_img rotate__0deg']"))
    image_90deg = selenium.PageElement(XPathQueryObject("//img[@class='photo-layer_img rotate__90deg']"))
    image_180deg = selenium.PageElement(XPathQueryObject("//img[@class='photo-layer_img rotate__180deg']"))
    image_270deg = selenium.PageElement(XPathQueryObject("//img[@class='photo-layer_img rotate__270deg']"))

    link = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='showLinkInput',
        )
    )

    delete_link = selenium.PageElement(XPathQueryObject("//a[@class='ic-w lp']"))
    restore_link = selenium.PageElement(XPathQueryObject("//a[@class='lp ml-2x']"))

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

    def next_photo(self):
        self.photo.wait(timeout=3)
        prev_size = self.photo.size
        self.next_arrow.wait(timeout=3)
        self.next_arrow.click()
        self.photo.wait(delay=3)
        return prev_size != self.photo.size

    def rotate_photo(self):
        self.photo.wait(timeout=3)
        if self.image_0deg.exist:
            self.rotate_link.click()
            self.image_90deg.wait(timeout=3)
            return self.image_90deg.exist
        elif self.image_90deg.exist:
            self.rotate_link.click()
            self.image_180deg.wait(timeout=3)
            return self.image_180deg.exist
        elif self.image_180deg.exist:
            self.rotate_link.click()
            self.image_270deg.wait(timeout=3)
            return self.image_270deg.exist
        elif self.image_270deg.exist:
            self.rotate_link.click()
            self.image_0deg.wait(timeout=3)
            return self.image_0deg.exist

    def delete_restore_photo(self):
        self.photo.wait(timeout=3)
        self.delete_link.wait(timeout=3)
        self.delete_link.click()
        self.restore_link.wait(timeout=3)
        if self.photo.is_displayed():
            self.restore_link.click()
            return False
        self.restore_link.click()
        self.photo.wait(delay=2)
        return self.photo.exist
