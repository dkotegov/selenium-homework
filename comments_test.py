import seismograph

from base_case import BaseCase
from  pages.video_page import VideoPage

suite = seismograph.Suite(__name__, require=['selenium'])

@suite.register
class CommentsCases(BaseCase):
    VIDEO_ID = '206460097000'
    COMMENT = 'TESTCOMMENT__TESTCOMMENT'

    def test_add_comment(self):
        video_page = VideoPage(self.browser)
        video_page.open(id=self.VIDEO_ID)

        video_page.add_comment(self.COMMENT)
        self.assertion.is_in(self.COMMENT, self.browser.page_source)

        video_page.delete_last_comment()
        self.browser.refresh()
        self.assertion.is_not_in(self.COMMENT, self.browser.page_source)



