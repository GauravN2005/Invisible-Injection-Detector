from fastapi import APIRouter
from pydantic import BaseModel

from app.services.policy_service import PolicyService

router = APIRouter(
    prefix="/policy",
    tags=["Policy Engine"]
)


class PolicyRequest(BaseModel):

    risk_score: float

    severity: str


class PolicyResponseModel(BaseModel):

    risk_score: float

    severity: str

    action: str


@router.post("/", response_model=PolicyResponseModel)
def evaluate(request: PolicyRequest):

    risk = {

        "risk_score": request.risk_score,

        "severity": request.severity

    }

    result = PolicyService.evaluate(risk)

    return PolicyResponseModel(**result)