# -*- coding: utf-8 -*-

import time

from elements.forms import NoteCreateForm
from elements.pages import NotesPage, RemoveStatusPopup
from seismograph.ext import selenium
from selenium.common.exceptions import NoSuchElementException
from tests.notes.utils import auth, get_note_text


suite = selenium.Suite(__name__)


@suite.register
def test_in_status(case, browser):
    """
        Добавляем несколько заметок.
        Проставлям их по очереди в статус.
        Удаляем заметки.
    """

    auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()

    notes_page.open_note_input()
    time.sleep(1)
    note_form = NoteCreateForm(browser)
    note_text = get_note_text()
    note_form.send_keys_in_last_text_form(note_text)
    note_form.submit()
    time.sleep(2)

    status_note = notes_page.get_status_note()
    case.assertion.equal(note_text, status_note.get_text())

    status_note.remove_from_status()
    time.sleep(1)
    confirm_popup = RemoveStatusPopup(browser)
    confirm_popup.submit()
    time.sleep(1)

    with case.assertion.raises(NoSuchElementException):
        notes_page.get_status_note().get_text()

    notes_page.open_note_input()
    time.sleep(1)
    note_form = NoteCreateForm(browser)
    note_text = get_note_text()
    note_form.send_keys_in_last_text_form(note_text)
    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(2)

    notes_page.get_last_note().in_status()

    status_note = notes_page.get_status_note()
    case.assertion.equal(note_text, status_note.get_text())

    notes_page.refresh()
    time.sleep(1)

    status_note.remove_from_status()
    time.sleep(1)
    confirm_popup = RemoveStatusPopup(browser)
    confirm_popup.submit()
    time.sleep(1)

    notes_page.remove_all_notes()

    notes_page.refresh()
    time.sleep(1)

    case.assertion.equal(0, notes_page.get_note_count())
