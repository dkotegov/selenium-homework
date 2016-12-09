from seismograph.ext import selenium


class NoteInput(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        id='hook_Block_PostingForm',
    )


class InStatusCheckbox(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='posting-form_ac-status'
    )

    unchecked = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class='irc',
        ),
        call=lambda checkbox: checkbox.click()
    )
