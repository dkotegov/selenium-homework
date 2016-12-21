# -*- coding: utf-8 -*-

from conf.base import USERNAME, PASSWORD
from seismograph.ext import selenium
from seismograph.ext.selenium import forms
from elements.items import InStatusCheckbox, NoteCreateFormAddedText, NoteCreateFormControls, NoteCreateFormAddedAudio, \
    NoteCreateFormAddedPhoto, NoteCreateFormActions, NoteCreateFormPlaceSelect, NoteCreateFormUserSelect


class AuthForm(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class=selenium.query.contains('anonym_login')
    )

    login_field = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_email'
        ),
    )

    password_field = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_password'
        ),
    )

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            value=u'Войти',
            type='submit'
        ),
        call=lambda btn: btn.click(),
    )

    def fill(self):
        self.login_field.send_keys(USERNAME)
        self.password_field.send_keys(PASSWORD)


class NoteCreateForm(forms.UIForm):

    added_text_fields = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='posting-form_sctn_w'
        ),
        is_list=True,
        we_class=NoteCreateFormAddedText
    )

    added_audio = selenium.PageElement(NoteCreateFormAddedAudio)

    added_photos = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('posting-form_sctn_w')
        ),
        is_list=True,
        we_class=NoteCreateFormAddedPhoto
    )

    in_status = selenium.PageElement(InStatusCheckbox)

    controls = selenium.PageElement(NoteCreateFormControls)

    actions = selenium.PageElement(NoteCreateFormActions)

    place_select = selenium.PageElement(NoteCreateFormPlaceSelect)

    user_select = selenium.PageElement(NoteCreateFormUserSelect)

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            value=u'Поделиться',
            type='submit'
        ),
        call=lambda btn: btn.click()
    )

    def wait_for_open(self):
        self.submit.wait()

    def send_keys_in_last_text_form(self, text):
        self.added_text_fields[-1].text_input.send_keys(text)

    def delete_last_added_text_form(self):
        self.added_text_fields[-1].delete()

    def delete_last_added_audio(self):
        return self.added_audio.delete_last()

    def delete_last_added_photo_in_block(self):
        self.added_photos[1].delete_last_inside_block()

    def delete_last_added_photo_block(self):
        self.added_photos[1].delete()
