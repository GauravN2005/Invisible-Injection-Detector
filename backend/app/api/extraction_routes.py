from fastapi import APIRouter
from pydantic import BaseModel

from app.services.extractor_service import ContentExtractor

router = APIRouter()


class ExtractionRequest(BaseModel):

    file_type: str

    content: str


@router.post("/extract")
def extract(request: ExtractionRequest):

    text = ContentExtractor.extract(
        request.content,
        request.file_type
    )

    return {
        "extracted_text": text
    }