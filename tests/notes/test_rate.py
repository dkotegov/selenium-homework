# -*- coding: utf-8 -*-

import time

from elements.forms import NoteCreateForm
from elements.items import NotePopup
from elements.pages import NotesPage
from seismograph.ext import selenium
from tests.notes.utils import auth, get_note_text


suite = selenium.Suite(__name__)


@suite.register
def test_rate(case, browser):
    """
        Добавляем заметку.
        Проверяем, что можно поставить и снять "Класс" несколькими вариантами.
        Удаляем заметку.
    """

    auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()

    notes_page.open_note_input()
    time.sleep(1)
    note_form = NoteCreateForm(browser)
    note_form.send_keys_in_last_text_form(get_note_text())
    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(2)

    last_note = notes_page.get_last_note()
    last_note.actions.like()
    time.sleep(1)
    case.assertion.equal(1, last_note.actions.get_like_count())

    last_note.actions.unlike()
    time.sleep(1)
    case.assertion.equal(0, last_note.actions.get_like_count())

    last_note.open()
    time.sleep(1)
    note_popup = NotePopup(browser)
    case.assertion.equal(0, note_popup.actions.get_like_count())

    note_popup.actions.like()
    time.sleep(1)
    case.assertion.equal(1, last_note.actions.get_like_count())

    note_popup.close()
    time.sleep(1)

    case.assertion.equal(1, last_note.actions.get_like_count())

    last_note.delete()
    time.sleep(1)

    notes_page.refresh()
    time.sleep(1)

    case.assertion.equal(0, notes_page.get_note_count())
