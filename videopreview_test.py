from base_case import BaseCase
import time
from pages.newvideos_page import NewVideos
from pages.video_page import VideoPage


class VideoPreviewTest(BaseCase):

    def test_openclose(self):
        newvideos_page = NewVideos(self.driver)
        newvideos_page.open()

        newvideos_page.open_first_video()
        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        self.assertIn('/video/', self.driver.current_url)
        # self.assertTrue('/video/' in self.driver.current_url)

        videoplayer_page.close_video()
        self.assertIn('/video/new', self.driver.current_url)
        # self.assertTrue('/video/new' in self.driver.current_url)

    def test_open_in_newtab(self):
        newvideos_page = NewVideos(self.driver)
        newvideos_page.open()

        newvideos_page.open_first_video()
        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        time.sleep(5)
        videoplayer_page.open_related_video_in_new_tab()
        time.sleep(5)
