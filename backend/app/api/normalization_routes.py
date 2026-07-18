from fastapi import APIRouter
from pydantic import BaseModel

from app.services.normalization_service import NormalizationService

router = APIRouter(
    prefix="/normalize",
    tags=["Normalization"]
)


class NormalizeRequest(BaseModel):
    text: str


class NormalizeResponse(BaseModel):
    original: str
    normalized: str


@router.post("/", response_model=NormalizeResponse)
def normalize(request: NormalizeRequest):
    """
    Normalize the input text by removing hidden characters,
    decoding HTML entities, cleaning markdown,
    and normalizing whitespace.
    """

    normalized_text = NormalizationService.process(request.text)

    return NormalizeResponse(
        original=request.text,
        normalized=normalized_text
    )