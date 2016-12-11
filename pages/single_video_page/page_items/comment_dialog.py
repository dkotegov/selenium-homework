from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil


class CommentDialog(PageItem):

    __area__ = query(
        query.DIV,
        _class=query.contains('mdialog')
    )

    el_close = PageElement(
        query(
            query.DIV,
            _class=query.contains('mdialog_disc_controls_close')
        )
    )

    def get_last_cmnt_text(self):
        X_PATH = "(.//div[contains(@class,'d_comment_text')])[last()]"
        cmnt = self.we.find_element_by_xpath(X_PATH)
        return cmnt.text

    def close(self):
        self.el_close.we.click()