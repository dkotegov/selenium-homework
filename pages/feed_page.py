# coding=utf-8
from seismograph.ext import selenium


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.ANY,
            id='viewImageLinkId'
        )
    )

    photo_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='mctc_navMenuSec'
        )
    )

    photo_check = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='hook_Block_UserAlbumStreamBlock',
        )
    )

    def goto_photo(self):
        self.photo_link.wait(timeout=3)
        self.photo_link.get(1).click()
        self.photo_check.wait(timeout=3)
        return self.photo_check.exist

