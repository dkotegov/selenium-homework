# -*- coding: utf-8 -*-
import random
import time

from conf.base import OK_URL
from elements.forms import AuthForm


def auth(browser):
    browser.go_to(OK_URL)

    auth_form = AuthForm(browser)
    auth_form.fill()
    auth_form.submit()

    time.sleep(3)


def get_note_text():
    return u'TEST NOTE - ТЕСТОВАЯ ЗАМЕТКА - {0}'.format(random.randint(0, 1000))
