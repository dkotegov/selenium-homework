import seismograph
from conf.base import OK_URL
from seismograph.ext import selenium
from elements.pages import AuthPage, NotesPage, UserPage


class AuthStep(selenium.Case):

    @seismograph.step(1, 'OK authorization')
    def auth(self, browser):
        browser.go_to(OK_URL)

        auth_page = AuthPage(browser)
        auth_page.wait_for_open()
        auth_page.authorize()

        user_page = UserPage(browser)
        user_page.wait_for_open()


class OpenNotesPageStep(selenium.Case):

    @seismograph.step(2, 'Go to my notes')
    def open_notes_page(self, browser):
        notes_page = NotesPage(browser)
        notes_page.open()
        notes_page.wait_for_open()
        notes_page.remove_all_notes()
        notes_page.refresh()
        notes_page.wait_for_open()
