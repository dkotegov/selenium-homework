# coding=utf-8
import seismograph

from pages.channel_page import ChannelPage
from pages.video_page import VideoPage
from tests.base_case import BaseCase

suite = seismograph.Suite(__name__, require=['selenium'])

TEST_CHANNEL_ID = '1567208'
TEST_VIDEO_ID = '206523142632'

@suite.register
class VideoOpenCase(BaseCase):

    def test_openclose(self):
        videos_page = ChannelPage(self.browser)
        videos_page.open(id=TEST_CHANNEL_ID)
        videos_page.open_video_by_id(TEST_VIDEO_ID)
        self.assertion.is_in(TEST_VIDEO_ID, self.browser.current_url)
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.close_video()
        self.assertion.is_not_in(TEST_VIDEO_ID, self.browser.current_url)

@suite.register
class VideoPreviewCase(BaseCase):

    def setup(self):
        super(VideoPreviewCase, self).setup()
        self.videoplayer_page = VideoPage(self.browser)
        self.videoplayer_page.open(id=TEST_VIDEO_ID)

    def test_open_in_newtab(self):
        url_related_video = self.videoplayer_page.get_url_related_video()
        self.videoplayer_page.open_related_video_in_new_tab()
        self.assertion.equal(url_related_video, self.browser.current_url) #bug in ok.ru here

    def test_video_plays(self):
        # self.videoplayer_page.pause_video()
        # self.videoplayer_page.rewind_video(0)
        time1 = self.videoplayer_page.get_video_play_time()
        self.videoplayer_page.play_video_during(1)
        time2 = self.videoplayer_page.get_video_play_time()
        self.assertion.not_equal(time1, time2)
    
    def test_video_pauses(self):
        self.videoplayer_page.pause_video()
        self.assertion.false(self.videoplayer_page.is_video_playing())

    def test_video_stops(self):
        self.videoplayer_page.stop_video()
        self.assertion.true(self.videoplayer_page.is_cover_visible())

    def test_next_video(self):
        next_video_url = self.videoplayer_page.play_next_video()
        self.assertion.not_equal(next_video_url, self.browser.current_url)

    def test_video_rewind(self):
        VIDEO_MIDDLE = 50

        self.videoplayer_page.rewind_video(0)
        self.videoplayer_page.pause_video()
        begin_time = self.videoplayer_page.get_video_play_time()
        self.videoplayer_page.rewind_video(VIDEO_MIDDLE)
        self.assertion.not_equal(self.videoplayer_page.get_video_play_time(), begin_time)

    def test_video_fullscreen(self):
        self.videoplayer_page.pause_video()
        width_original = self.videoplayer_page.get_video_window_size()['width']
        self.videoplayer_page.open_fullscreen()
        width_fullscreen = self.videoplayer_page.get_video_window_size()['width']
        self.assertion.greater(width_fullscreen, width_original)
        self.videoplayer_page.close_fullscreen()
        width_current = self.videoplayer_page.get_video_window_size()['width']
        self.assertion.equal(width_original, width_current)

    def test_video_widescreen(self):
        self.videoplayer_page.pause_video()
        width_original = self.videoplayer_page.get_video_window_size()['width']

        self.videoplayer_page.open_widescreen()
        width_widescreen = self.videoplayer_page.get_video_window_size()['width']
        self.assertion.greater(width_widescreen, width_original)

    def test_video_miniscreen(self):
        self.videoplayer_page.pause_video()
        width_original = self.videoplayer_page.get_video_window_size()['width']

        self.videoplayer_page.rollin_video()
        width_miniscreen = self.videoplayer_page.get_video_window_size()['width']
        self.assertion.greater(width_original, width_miniscreen)

    def test_get_video_url(self):
        url = self.videoplayer_page.get_video_url()
        self.assertion.equal(url, self.browser.current_url)