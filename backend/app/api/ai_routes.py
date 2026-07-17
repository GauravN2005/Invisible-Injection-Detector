from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import AIService

router = APIRouter(
    prefix="/detect",
    tags=["AI Detection"]
)


class DetectionRequest(BaseModel):
    text: str


class DetectionResponse(BaseModel):

    prediction: str

    confidence: float

    matches: list[str]


@router.post("/", response_model=DetectionResponse)
def detect(request: DetectionRequest):

    result = AIService.analyze(request.text)

    return DetectionResponse(**result)