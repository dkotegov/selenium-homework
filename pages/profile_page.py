from seismograph.ext import selenium
import utils

class ProfilePage(selenium.Page):

    name = utils.query('ANY', _class='mctc_name_tx bl')