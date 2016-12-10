# coding=utf-8
import seismograph

from base_case import BaseCase
import time
from pages.channel_page import ChannelPage
# from pages.suggestedvideos_page import SuggestedVideos
from pages.video_page import VideoPage

suite = seismograph.Suite(__name__, require=['selenium'])

TEST_CHANNEL_ID = '1567208'
TEST_VIDEO_ID = '206523142632'

@suite.register
class VideoPreviewTest(BaseCase):

    def setup(self):
        super(VideoPreviewTest, self).setup()
        self.videos_page = ChannelPage(self.browser)
        self.videos_page.open(id= TEST_CHANNEL_ID)
        self.videos_page.open_video_by_id(TEST_VIDEO_ID)

    def test_openclose(self):
        self.assertion.is_in(TEST_VIDEO_ID, self.browser.current_url)
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.close_video()
        self.assertion.is_not_in(TEST_VIDEO_ID, self.browser.current_url)

    def test_open_in_newtab(self):
        videoplayer_page = VideoPage(self.browser)
        url_related_video = videoplayer_page.get_url_related_video()
        videoplayer_page.open_related_video_in_new_tab()
        self.assertion.equal(url_related_video, self.browser.current_url) #bug in ok.ru here

    def test_video_plays(self):
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.play_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertion.not_equal(time1, time2)

    def test_video_pauses(self):
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.pause_video()
        time1 = videoplayer_page.get_video_play_time()
        time.sleep(3)
        time2 = videoplayer_page.get_video_play_time()
        self.assertion.equal(time1, time2)

    def test_video_stops(self):
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.stop_video()
        self.assertion.true(videoplayer_page.is_cover_visible())

    def test_next_video(self):
        videoplayer_page = VideoPage(self.browser)
        previous_url = self.browser.current_url
        videoplayer_page.play_next_video()
        #nextvideo_page = VideoPage(self.browser)
        self.assertion.not_equal(previous_url, self.browser.current_url)
        # TODO Заранее получать ссылку следующего видео и сравнивать с ней

    def test_video_rewind(self):#TODO ELEMENT NOT VISIBLE
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.pause_video()
        begin_time = videoplayer_page.get_video_play_time()
        videoplayer_page.rewind_video(50)
        self.assertion.not_equal(videoplayer_page.get_video_play_time(), begin_time)

    def test_video_fullscreen(self):
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.pause_video()
        width_original = videoplayer_page.get_video_window_size()['width']
        videoplayer_page.open_fullscreen()
        width_fullscreen = videoplayer_page.get_video_window_size()['width']
        self.assertion.greater(width_fullscreen, width_original)
        videoplayer_page.close_fullscreen()
        width_current = videoplayer_page.get_video_window_size()['width']
        self.assertion.equal(width_original, width_current)
