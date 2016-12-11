from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil
from .attach_video_dialog import AttachVideoDialog
from .attach_photo_dialog import AttachPhotoDialog
import utils


class VideoCommentForm(PageItem):

    __area__ = query(
        query.DIV,
        _id='movie-comments'
    )

    class InputField(PageItem):

        def set_text(self, text):
            ScriptUtil.click_directly_seismograph(self.browser, self.we)
            ScriptUtil.set_text_directly_seismograph(self.browser, self.we, text)
            #self.we.click()
            #self.we.send_keys(text)

    el_input = PageElement(
        query(
            query.DIV,
            _class=query.contains('js-comments_add')
        ),
        we_class=InputField
    )

    class SendBtn(PageItem):

        def send(self):
            ScriptUtil.click_directly_seismograph(self.browser, self.we)
            #self.we.click()

    el_send_btn = PageElement(
        query(
            query.BUTTON,
            _class=query.contains('form-actions_yes')
        ),
        we_class=SendBtn
    )

    class AttachVideo(PageItem):

        def attach_click(self):
            x_path = "//span[@class='comments_attach_trigger']//ul[@class='u-menu']/li[1]/a"
            driver = self.browser._wrapped
            lst = utils.wait_many_xpath(driver, x_path)
            elem = lst[-1]
            ScriptUtil.click_directly(driver, elem)

    el_attach_video = PageElement(
        query(
            query.A,
            _href=query.startswith('/feed')
        ),
        we_class=AttachVideo
    )

    class AttachPhoto(PageItem):

        def attach_click(self):
            x_path = "//span[@class='comments_attach_trigger']//ul[@class='u-menu']/li[2]/a/span"
            driver = self.browser._wrapped
            lst = utils.wait_many_xpath(driver, x_path)
            elem = lst[-1]
            ScriptUtil.click_directly(driver, elem)

    el_attach_photo = PageElement(
        query(
            query.A,
            _class=query.contains('u-menu_a'),
            _href=query.startswith('javascript')
        ),
        we_class=AttachPhoto
    )

    class AttachPhotoFromPc(PageItem):

        def attach_click(self, path):
            self.we.send_keys(path)

    el_attach_photo_from_pc = PageElement(
        query(
            query.INPUT,
            _class=query.contains('h-mod html5-upload-link')
        ),
        we_class=AttachPhotoFromPc
    )

    def attach_video_in_dialog(self):
        self.el_attach_video.attach_click()
        dialog = PageElement(AttachVideoDialog)
        dialog.el_video.click_video()

    def attach_photo_in_dialog(self):
        self.el_attach_photo.attach_click()
        dialog = AttachPhotoDialog(self.browser)
        dialog.el_photo.click_photo()
        dialog.el_add_btn.click_btn()

    def attach_photo_from_pc(self, path):
        self.el_attach_photo_from_pc.attach_click(path)

    def set_text(self, text):
        self.el_input.set_text(text)

    def submit(self):
        self.el_send_btn.send()
