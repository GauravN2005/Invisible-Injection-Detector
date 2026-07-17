from fastapi import APIRouter
from pydantic import BaseModel

from app.services.risk_service import RiskService

router = APIRouter(
    prefix="/risk",
    tags=["Risk Scoring"]
)


class RiskRequest(BaseModel):

    confidence: float

    matches: list[str]


class RiskResponse(BaseModel):

    risk_score: float

    severity: str


@router.post("/", response_model=RiskResponse)
def calculate(request: RiskRequest):

    ai_result = {
        "confidence": request.confidence,
        "matches": request.matches
    }

    result = RiskService.evaluate(ai_result)

    return RiskResponse(**result)