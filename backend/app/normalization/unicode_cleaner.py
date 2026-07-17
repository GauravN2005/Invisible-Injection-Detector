import re
import unicodedata


ZERO_WIDTH_PATTERN = re.compile(
    r'[\u200B-\u200D\u2060\uFEFF]'
)


def clean_unicode(text: str) -> str:
    """
    Remove invisible Unicode characters and normalize Unicode.
    """

    # Unicode Normalization
    text = unicodedata.normalize("NFKC", text)

    # Remove zero-width characters
    text = ZERO_WIDTH_PATTERN.sub("", text)

    return text