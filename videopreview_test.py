from base_case import BaseCase
import utils
from pages.newvideos_page import NewVideos
from pages.video_page import VideoPage


class VideoPreviewTest(BaseCase):

    def test_openclose(self):
        newvideos_page = NewVideos(self.driver)
        newvideos_page.open()

        video_link = newvideos_page.open_first_video()
        self.assertIn(video_link, self.driver.current_url)

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.close_video()
        self.assertIn(newvideos_page.PATH , self.driver.current_url)
