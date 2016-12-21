# -*- coding: utf-8 -*-

import time

from elements.forms import NoteCreateForm
from elements.items import NotePopup
from elements.pages import NotesPage
from seismograph.ext import selenium
from tests.notes.utils import get_note_text


suite = selenium.Suite(__name__)


@suite.register
def test_edit(case, browser):
    """
        Добавляем заметку.
        Редактируем, проверяем изменения.
        Удаляем заметку.
    """

    auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    time.sleep(1)
    notes_page.remove_all_notes()

    notes_page.open_note_create_form()
    time.sleep(1)
    note_form = NoteCreateForm(browser)
    first_text = get_note_text()
    note_form.send_keys_in_last_text_form(first_text)
    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(2)

    last_note = notes_page.get_last_note()
    last_note.open()
    time.sleep(1)
    note_popup = NotePopup(browser)
    second_text = get_note_text()
    note_popup.edit_note(second_text)
    time.sleep(1)

    note_popup.close()
    time.sleep(1)

    notes_page.refresh()
    time.sleep(1)

    last_note = notes_page.get_last_note()
    expected_text = u'{0}{1}'.format(first_text, second_text)
    final_text = notes_page.get_last_note().get_text()

    case.assertion.equal(expected_text, final_text)

    last_note.delete()
    time.sleep(1)

    notes_page.refresh()
    time.sleep(1)

    case.assertion.equal(0, notes_page.get_note_count())
