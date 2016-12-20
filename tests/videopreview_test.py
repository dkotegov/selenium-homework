# coding=utf-8
import seismograph

from pages.channel_page import ChannelPage
from pages.video_page import VideoPage
from tests.base_case import BaseCase

suite = seismograph.Suite(__name__, require=['selenium'])



@suite.register
class VideoOpenCase(BaseCase):
    VIDEO_ID = '206699762152'
    CHANNEL_ID = '1567208'

    def test_openclose(self):
        
        videos_page = ChannelPage(self.browser)
        videos_page.open(id=self.CHANNEL_ID)
        videos_page.open_video_by_id(self.VIDEO_ID)
        self.assertion.is_in(self.VIDEO_ID, self.browser.current_url)
        videoplayer_page = VideoPage(self.browser)
        videoplayer_page.close_video()
        self.assertion.is_not_in(self.VIDEO_ID, self.browser.current_url)


@suite.register
class VideoPreviewCase(BaseCase):
    VIDEO_ID = '218249104011'

    def setup(self):
        super(VideoPreviewCase, self).setup()
        self.videoplayer_page = VideoPage(self.browser)
        self.videoplayer_page.open(id=self.VIDEO_ID)

    @seismograph.skip('Bug in OK')
    def test_open_in_newtab(self):
        url_related_video = self.videoplayer_page.get_url_related_video()
        self.videoplayer_page.open_related_video_in_new_tab()
        self.assertion.equal(url_related_video, self.browser.current_url)  # bug in ok.ru here

    def test_video_plays(self):
        time1 = self.videoplayer_page.get_video_play_time()
        self.videoplayer_page.play_video_during(1)
        time2 = self.videoplayer_page.get_video_play_time()
        self.assertion.not_equal(time1, time2)

    def test_video_pauses(self):
        self.videoplayer_page.pause_video()
        self.assertion.false(self.videoplayer_page.is_video_playing())

    def test_next_video(self):
        next_video_url = self.videoplayer_page.play_next_video()
        self.assertion.not_equal(next_video_url, self.browser.current_url)

    def test_video_rewind(self):
        self.videoplayer_page.pause_video()
        begin_time = self.videoplayer_page.get_video_play_time()
        self.videoplayer_page.rewind_video()
        self.assertion.not_equal(self.videoplayer_page.get_video_play_time(), begin_time)

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
