from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from .page_item_base import PageItemBase


class InfoItem(PageItem):

    __area__ = query(
        query.DIV,
        _class='vp-layer-info'
    )

    el_video_name = PageElement(
        query(
            query.DIV,
            _class=query.contains('portlet_h')
        )
    )

    el_video_date = PageElement(
        query(
            query.DIV,
            _class='vp-layer-info_date'
        )
    )

    el_video_views = PageElement(
        query(
            query.DIV,
            _class='vp-layer-info_views'
        )
    )

    class CommentsLink(PageItem):

        X_CNT = "/span[contains(@class, 'widget_count')]"

        def get_comments_count(self):
            cnt = self.we.find_element_by_xpath(self.X_CNT)
            return cnt.txt

        def open(self):
            self.we.click()

    el_comments_link = PageElement(
        query(
            query.A,
            query.expression(
                _class=query.contains('widget_cnt'),
                _href=query.startswith('/discussions')
            )
        ),
        we_class=CommentsLink
    )

    el_klasses_btn = PageElement(
        query(
            query.BUTTON,
            query.expression(
                _class=query.contains('widget_cnt'),
                _href=query.startswith('/discussions')
            )
        ),
        we_class=CommentsLink
    )



class ChannelItem(PageItem):

    __area__ = query(
        query.DIV,
        _class='vp-layer-channel'
    )

    el_logo = PageElement(
        query(
            query.IMG,
            _class='ucard_img_cnt'
        )
    )

    el_album_link = PageElement(
        query(
            query.A,
            _class='js-video-album-link'
        )
    )

    el_author_link = PageElement(
        query(
            query.A,
            _class=query.startswith('/profile/')
        )
    )

    go_to_author_channel = PageElement(
        el_author_link,
        call=lambda we: we.click()
    )


class DescriptionItem(PageItem):

    __area__ = query(
        query.DIV,
        _class='vp-layer-description'
    )

    css_expand = 'js-vp-layer-description_more'
    el_expand = PageElement(
        query(
            query.SPAN,
            _class=query.contains(css_expand)
        )
    )

    do_expand = PageElement(
        el_expand,
        call=lambda we: we.click()
    )

    def check_expanded(self):
        #el_expand = self.browser.span(_class=query.contains(self.css_expand))
        css_cls = self.el_expand.attr._class
        if css_cls.contains('invisible'):
            return True
        return False
