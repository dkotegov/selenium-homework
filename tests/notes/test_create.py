# -*- coding: utf-8 -*-
import random

import time

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
    NOTE_TEXT = u'TEST NOTE - ТЕСТОВАЯ ЗАМЕТКА - {0}'.format(random.randint(0, 100))

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()

    note_form = NoteCreateForm(browser)
    note_form.note_text_field.send_keys(NOTE_TEXT)
    note_form.in_status.unchecked()
    note_form.submit()

    time.sleep(3)
    notes_page.refresh()
    case.assertion.equal(notes_page.get_last_note().get_text(), NOTE_TEXT)

    notes_page.get_last_note().delete()





