import seismograph

from base_case import BaseCase
from pages.newvideos_page import NewVideos
from pages.video_page import VideoPage

suite = seismograph.Suite(__name__, require=['selenium'])


#@suite.register
class VideoPreviewTest(BaseCase):
    def test_openclose(self):
        newvideos_page = NewVideos(self.browser)
        newvideos_page.open()

        video_link = newvideos_page.open_first_video()
        self.assertion.is_in(video_link, self.browser.current_url)

        video_id = video_link.split('/')[-1]
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.open(id=video_id)
        videoplayer_page.close_video_button.click()
        self.assertion.is_not_in(video_link, self.browser.current_url)
