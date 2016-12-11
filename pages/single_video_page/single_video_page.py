from seismograph.ext.selenium import Page, PageItem, PageElement, query
from pages.single_video_page.page_items.video_meta import InfoItem, ChannelItem, DescriptionItem
from .page_items.video_comment_form import VideoCommentForm
from .page_items.video_last_comment import LastComment
from .page_items.comment_dialog import CommentDialog


class SingleVideoPage(Page):

    __url_path__ = "/video/{id}"

    info_item = PageElement(InfoItem)
    channel_item = PageElement(ChannelItem)
    description_item = PageElement(DescriptionItem)

    close_icon = PageElement(
        query(
            query.DIV,
            _class=query.contains('media-layer_close_ico')
        )
    )

    minimize_icon = PageElement(
        query(
            query.DIV,
            _class=query.contains('media-layer_turn_ico')
        )
    )

    def send_comment(self, with_photo=False, with_video=False, text="123"):
        form = VideoCommentForm(self.browser)
        if with_photo:
            form.attach_photo_in_dialog()
        if with_video:
            form.attach_video_in_dialog()
        form.set_text(text)
        form.submit()
        self.refresh()

    def get_last_comment(self):
        cmnt = LastComment(self.browser)
        return cmnt

    def get_last_comment_text_from_dialog(self):
        self.info_item.el_comments_link.open()
        cmnt_dialog = CommentDialog(self.browser)
        text = cmnt_dialog.get_last_cmnt_text()
        cmnt_dialog.close()
        return text

    def get_comments_count(self):
        return self.info_item.el_comments_link.get_comments_count()

    def answer_last_comment(self, text):
        cmnt = self.get_last_comment()
        cmnt.el_reply.we.click()
        self.send_comment(with_photo=False, with_video=False, text=text)
