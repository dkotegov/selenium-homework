from seismograph.ext import selenium


class CommentPage(selenium.Page):
    comment_body = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='topPanelPopup_d'
        )
    )

    comment_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d'
        )
    )
