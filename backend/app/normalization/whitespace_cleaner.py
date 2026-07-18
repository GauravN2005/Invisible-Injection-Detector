import re


def clean_whitespace(text: str) -> str:
    """
    Remove extra spaces, tabs and newlines.
    """

    text = re.sub(r"\s+", " ", text)

    return text.strip()