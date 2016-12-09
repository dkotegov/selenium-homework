# -*- coding: utf-8 -*-

import os
from seismograph.ext import selenium
from seismograph.ext.selenium import forms
from utils.items import InStatusCheckbox


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

    note_text_field = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='posting_form_text_field'
        )
    )

    in_status = selenium.PageElement(InStatusCheckbox)

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            value=u'Поделиться',
            type='submit'
        ),
        call=lambda btn: btn.click(),
    )
