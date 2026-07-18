import re


def clean_markdown(text: str) -> str:
    """
    Remove common Markdown syntax while preserving text.
    """

    # Remove bold/italic markers
    text = re.sub(r'[*_`#>]', '', text)

    # Remove markdown links but keep the visible text
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)

    return text