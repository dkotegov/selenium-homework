# -*- coding: utf-8 -*-

import os
from seismograph.ext import selenium
from seismograph.ext.selenium import forms


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
