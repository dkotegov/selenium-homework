# -*- coding: utf-8 -*-

from conf.base import OK_URL
from seismograph.ext import selenium
from utils.forms import AuthForm, NoteCreateForm
from utils.pages import NotesPage


suite = selenium.Suite(__name__)


def _auth(browser):
    browser.go_to(OK_URL)

    auth_form = AuthForm(browser)
    auth_form.fill()
    auth_form.submit()


@suite.register
def test_create_with_text_boxes(case, browser):
    NOTE_TEXT = u'TEST NOTE - ТЕСТОВАЯ ЗАМЕТКА'

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open_note_input()

    note_form = NoteCreateForm(browser)
    note_form.note_text_field.send_keys(NOTE_TEXT)
    note_form.in_status.unchecked()
    note_form.submit()




