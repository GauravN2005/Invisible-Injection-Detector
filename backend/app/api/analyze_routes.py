from fastapi import APIRouter
from pydantic import BaseModel

from app.services.analyze_service import AnalyzeService

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"]
)


class AnalyzeRequest(BaseModel):
    file_type: str
    content: str


class AnalyzeResponse(BaseModel):
    original_text: str
    extracted_text: str
    normalized_text: str
    prediction: str
    prediction_confidence: float
    attack_probability: float
    matches: list[str]
    risk_score: float
    severity: str
    action: str


@router.post("/", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):

    return AnalyzeService.analyze(
        request.file_type,
        request.content
    )