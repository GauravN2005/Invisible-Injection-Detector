from app.normalization.unicode_cleaner import clean_unicode
from app.normalization.html_cleaner import clean_html
from app.normalization.whitespace_cleaner import clean_whitespace
from app.normalization.markdown_cleaner import clean_markdown


class InputNormalizer:

    @staticmethod
    def normalize(text: str) -> str:

        text = clean_unicode(text)

        text = clean_html(text)

        text = clean_markdown(text)

        text = clean_whitespace(text)

        return text