from base_case import BaseCase
import time
from pages.suggestedvideos_page import SuggestedVideos
from pages.video_page import VideoPage


class VideoPreviewTest(BaseCase):

    def test_openclose(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()

        video_link = videos_page.open_first_video()
        self.assertIn(video_link, self.driver.current_url)

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.close_video()
        self.assertIn(videos_page.PATH, self.driver.current_url)

    def test_open_in_newtab(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        url_related_video = videoplayer_page.get_url_related_video()
        videoplayer_page.open_related_video_in_new_tab()
        self.assertEqual(url_related_video, self.driver.current_url) #bug in ok.ru here

    def test_video_plays(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.play_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertNotEqual(time1, time2)

    def test_video_pauses(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.pause_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertEqual(time1, time2)

    def test_video_stops(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.stop_video()
        self.assertTrue(videoplayer_page.is_cover_visible())

    def test_next_video(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.play_next_video()
        nextvideo_page = VideoPage(self.driver, self.driver.current_url)
        self.assertNotEqual(videoplayer_page.PATH, nextvideo_page.PATH)

    def test_video_rewind(self):
        videos_page = SuggestedVideos(self.driver)
        videos_page.open()
        videos_page.open_first_video()

        videoplayer_page = VideoPage(self.driver, self.driver.current_url)
        videoplayer_page.pause_video()
        begin_time = videoplayer_page.get_video_play_time()
        videoplayer_page.rewind_video(50)
        self.assertNotEqual(videoplayer_page.get_video_play_time(), begin_time)

