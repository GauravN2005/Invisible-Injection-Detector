import html


def clean_html(text: str) -> str:
    """
    Decode HTML entities.
    """

    return html.unescape(text)