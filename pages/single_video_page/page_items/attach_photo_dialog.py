from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil


class AttachPhotoDialog(PageItem):

    __area__ = query(
        query.DIV,
        _class=query.contains('modal-new_center')
    )

    class Photo(PageItem):

        def click_photo(self):
            self.we.click()

    el_photo = PageElement(
        query(
            query.DIV,
            _class=query.contains('photo-crop_cnt selectable-card')
        ),
        we_class=Photo
    )

    class AddButton(PageItem):

        def click_btn(self):
            self.we.click()

    el_add_btn = PageElement(
        query(
            query.INPUT,
            _id=query.contains('hook_FormButton_button_attach')
        ),
        we_class=AddButton
    )
