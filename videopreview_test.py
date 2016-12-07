from base_case import BaseCase
import utils
from pages.newvideos_page import NewVideos
from pages.video_page import VideoPage


class VideoPreviewTest(BaseCase):

    def test_openclose(self):
        newvideos_page = NewVideos(self.driver)
        newvideos_page.open()

        newvideos_page.open_first_video()
        self.assertTrue('/video/' in self.driver.current_url)

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.close_video()
        self.assertTrue('/video/new' in self.driver.current_url)
