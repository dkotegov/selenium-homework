from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject


class AlbumPage(selenium.Page):
    album = selenium.PageElement(XPathQueryObject("//li[@class='ugrid_i'][3]"))
    edit = selenium.PageElement(XPathQueryObject("//div[@class='photo-menu_edit iblock-cloud_show']"))
    delete = selenium.PageElement(XPathQueryObject("//li[@class='controls-list_item'][2]"))
    confirm_delete = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='hook_FormButton_button_delete_confirm',
        )
    )
    add_album = selenium.PageElement(XPathQueryObject("//span[@class='add-stub_tx']"))

    def delete_album(self):
        self.album.wait(timeout=3)
        self.album.click()
        self.edit.wait(timeout=3)
        self.edit.click()
        self.delete.wait(timeout=3)
        self.delete.click()
        self.confirm_delete.wait(timeout=3)
        self.confirm_delete.click()
        self.add_album.wait(timeout=3)
        return self.add_album.exist



