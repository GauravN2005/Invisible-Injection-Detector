from app.extraction.text_extractor import extract_text
from app.extraction.html_extractor import extract_html
from app.extraction.pdf_extractor import extract_pdf
from app.extraction.image_extractor import extract_image


class ContentExtractor:

    @staticmethod
    def extract(content, file_type):

        if file_type == "text":
            return extract_text(content)

        elif file_type == "html":
            return extract_html(content)

        elif file_type == "pdf":
            return extract_pdf(content)

        elif file_type == "image":
            return extract_image(content)

        else:
            raise ValueError("Unsupported file type")