# -*- coding: utf-8 -*-

import time

from elements.forms import NoteCreateForm
from elements.pages import NotesPage
from seismograph.ext import selenium
from tests.notes.utils import auth, get_note_text


suite = selenium.Suite(__name__)


@suite.register
def test_remove_and_restore(case, browser):
    """
        Добавляем несколько заметок.
        Удаляем все заметки и восстанавливаяем их назад.
        Удаляем заметки.
    """

    auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()

    note_count = 2
    for _ in range(note_count):
        notes_page.open_note_input()
        time.sleep(1)
        note_form = NoteCreateForm(browser)
        note_form.send_keys_in_last_text_form(get_note_text())
        note_form.in_status.unchecked()
        note_form.submit()
        time.sleep(2)

    case.assertion.equal(note_count, notes_page.get_note_count())

    for i in range(note_count):
        note = notes_page.get_note(i)
        text_before = note.get_text()
        note.delete()
        time.sleep(1)
        note.restore()
        time.sleep(1)
        text_after = note.get_text()
        case.assertion.equal(text_before, text_after)

    notes_page.remove_all_notes()

    notes_page.restore_all_notes()

    case.assertion.equal(note_count, notes_page.get_note_count())

    notes_page.remove_all_notes()

    notes_page.refresh()
    time.sleep(1)

    case.assertion.equal(0, notes_page.get_note_count())
