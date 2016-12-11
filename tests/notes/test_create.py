# -*- coding: utf-8 -*-

import random
import time

from conf.base import OK_URL, STATIC_PATH
from seismograph.ext import selenium
from utils.forms import AuthForm, NoteCreateForm
from utils.items import AddAudioPopup
from utils.pages import NotesPage


suite = selenium.Suite(__name__)


def _auth(browser):
    browser.go_to(OK_URL)

    auth_form = AuthForm(browser)
    auth_form.fill()
    auth_form.submit()

    time.sleep(3)


def _get_note_text():
    return u'TEST NOTE - ТЕСТОВАЯ ЗАМЕТКА - {0}'.format(random.randint(0, 1000))


@suite.register
def test_create_with_text_boxes(case, browser):
    """
        Заполняем случайным образом несколько текстовых форм.
        Удаляем одну из форм.
        Добавляем заметку, проверяем получившейся в ней текст.
        Удаляем заметку.
    """

    note_texts_count = 3

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()
    time.sleep(1)

    note_texts = []
    for i in range(0, note_texts_count + 2):
        note_texts.append(_get_note_text())

    note_form = NoteCreateForm(browser)
    note_form.send_keys_in_last_text_form(note_texts[0])
    for i in range(1, note_texts_count + 1):
        note_form.controls.add_text_form()
        note_form.send_keys_in_last_text_form(note_texts[i])

    note_form.delete_last_added_text_form()
    time.sleep(1)

    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(1)

    note_final_text = '\n'.join(note_texts[:-2])
    case.assertion.equal(notes_page.get_last_note().get_text(), note_final_text)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()


@suite.register
def test_create_with_photo(case, browser):
    """
        Создаем заметку с несколькими фотографиями разных форматов + некоторые из фото не валидны.
        Проверяем удаление фотографий внутри блока, а так же самого блока с фотографиями.
        Проверяем кол-во фотографий в созданной заметке.
        Удаляем заметку.
    """

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()
    time.sleep(1)

    note_form = NoteCreateForm(browser)
    photo_names = (
        'test-img.png',
        'test-img.png',
        'test-img.png',
        'test-img-small.png',
        'test-img.png',
        'test-img-small.png',
    )
    for name in photo_names:
        photo = '{0}img/{1}'.format(STATIC_PATH, name)
        note_form.controls.add_photo(photo)
        time.sleep(1)

    note_form.delete_last_added_photo_block()
    time.sleep(1)

    note_form.delete_last_added_photo_in_block()
    time.sleep(1)

    # Остается три валидных фото

    note_form.in_status.unchecked()
    note_form.submit()

    time.sleep(1)

    case.assertion.equal(notes_page.get_last_note().get_photo_count(), 3)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()


@suite.register
def test_create_with_audio(case, browser):
    """
        Выбираем случайным образом несколько аудиозаписей из поиска.
        Добавляем заметку, проверяем названия добавленных аудиозаписей.
        Проверяем возможность удаления аудиозаписей.
        Удаляем заметку.
    """

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()

    time.sleep(1)

    note_form = NoteCreateForm(browser)
    note_form.controls.add_audio()

    time.sleep(1)

    search_audio_name = u'Билан'
    add_audio_popup = AddAudioPopup(browser)
    add_audio_popup.search(search_audio_name)

    time.sleep(3)

    records_names = add_audio_popup.select_audio()

    time.sleep(1)

    add_audio_popup.add_audio()

    time.sleep(1)

    for _ in range(2):
        last_record_name = note_form.delete_last_added_audio()
        time.sleep(1)
        records_names.remove(last_record_name)

    note_form.in_status.unchecked()
    note_form.submit()

    time.sleep(1)

    expected_names = notes_page.get_last_note().get_audio_names()
    for name, expected_name in zip(sorted(records_names), sorted(expected_names)):
        case.assertion.is_in(name, expected_name)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()


@suite.register
def test_create_with_place(case, browser):
    """
        Добавляем заметку и указываем несколько мест, проверяя возможность их удаления.
        Проверяем наличие карты и правильные ли места.
        Удаляем заметку.
    """

    _auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()

    time.sleep(1)

    note_form = NoteCreateForm(browser)
    note_form.actions.add_place()

    time.sleep(1)

    expected_place_name = note_form.place_select.select_random_place()
    time.sleep(1)
    place_name = note_form.place_select.selected_place.get_name()
    case.assertion.equal(expected_place_name, place_name)

    note_form.place_select.remove_selected_place()
    time.sleep(1)

    search_place_name = u'Москва'
    note_form.actions.add_place()
    note_form.place_select.search(search_place_name)
    time.sleep(1)
    place_name = note_form.place_select.select_first_place()
    case.assertion.equal(search_place_name, place_name)
    time.sleep(1)

    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(1)

    expected_place_names = notes_page.get_last_note().get_place_names()
    case.assertion.is_in(place_name, expected_place_names)

    case.assertion.equal(notes_page.get_last_note().get_map_count(), 1)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()
