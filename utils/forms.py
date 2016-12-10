# -*- coding: utf-8 -*-

import os
from seismograph.ext import selenium
from seismograph.ext.selenium import forms
from utils.items import InStatusCheckbox, NoteCreateFormAddedText, NoteCreateFormControls, NoteCreateFormAddedAudio


class AuthForm(forms.UIForm):

    login_field = forms.fields.Input(
        'Login',
        value=os.environ['USERNAME'],
        selector=forms.fields.selector(id='field_email'),
    )

    password_field = forms.fields.Input(
        'Password',
        value=os.environ['PASSWORD'],
        selector=forms.fields.selector(id='field_password'),
    )

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            value=u'Войти',
            type='submit'
        ),
        call=lambda btn: btn.click(),
    )


class NoteCreateForm(forms.UIForm):

    note_text_fields = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='posting-form_sctn_w'
        ),
        is_list=True,
        we_class=NoteCreateFormAddedText
    )

    added_audio = selenium.PageElement(NoteCreateFormAddedAudio)

    in_status = selenium.PageElement(InStatusCheckbox)

    controls = selenium.PageElement(NoteCreateFormControls)

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            value=u'Поделиться',
            type='submit'
        ),
        call=lambda btn: btn.click()
    )

    def send_keys_in_last_text_form(self, text):
        self.note_text_fields[-1].text_input.send_keys(text)

    def delete_last_added_text_form(self):
        self.note_text_fields[-1].delete()

    def delete_last_added_audio(self):
        return self.added_audio.delete_last()
