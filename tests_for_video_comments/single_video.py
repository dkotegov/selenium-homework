import seismograph
from base_case import BaseCase
from pages.single_video_page.single_video_page import SingleVideoPage

suite = seismograph.Suite(__name__, require=['selenium'])

@suite.register
class Test1Case(BaseCase):

    def setup(self):
        super(Test1Case, self).setup()
        self.video_page = SingleVideoPage(self.browser)
        self.video_page.open(id=206458458600)

    def test1(self):
        self.video_page.description_item.do_expand()
        self.video_page.description_item.check_expanded()
        cmnts = self.video_page.info_item.el_comments_link.get_comments_count()
        self.video_page.info_item.el_klasses_btn.switch_klass()
        kls = self.video_page.info_item.el_klasses_btn.get_klasses_count()
        pass