from base_case import BaseCase
import time
from pages.suggestedvideos_page import SuggestedVideos
from pages.video_page import VideoPage


class VideoPreviewTest(BaseCase):

    def test_openclose(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()

        video_link = newvideos_page.open_first_video()
        self.assertIn(video_link, self.driver.current_url)

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.close_video()
        self.assertIn(newvideos_page.PATH, self.driver.current_url)

    def test_open_in_newtab(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()
        newvideos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        url_related_video = videoplayer_page.get_url_related_video()
        videoplayer_page.open_related_video_in_new_tab()
        self.assertEqual(url_related_video, self.driver.current_url) #bug in ok.ru here

    def test_video_plays(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()
        newvideos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.play_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertNotEqual(time1, time2)

    def test_video_pauses(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()
        newvideos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.pause_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertEqual(time1, time2)

    def test_video_stops(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()
        newvideos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.stop_video()
        self.assertTrue(videoplayer_page.is_cover_visible())

    def test_next_video(self):
        newvideos_page = SuggestedVideos(self.driver)
        newvideos_page.open()
        newvideos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.play_next_video()
        nextvideo_page = VideoPage(self.driver, self.driver.current_url)
        self.assertNotEqual(videoplayer_page.PATH, nextvideo_page.PATH)

