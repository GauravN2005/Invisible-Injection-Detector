from fastapi import FastAPI

from app.api.extraction_routes import router as extraction_router
from app.api.normalization_routes import router as normalization_router
from app.api.ai_routes import router as ai_router
from app.api.risk_routes import router as risk_router
from app.api.policy_routes import router as policy_router
from app.api.analyze_routes import router as analyze_router

app = FastAPI(
    title="Invisible Injection Detector"
)

app.include_router(extraction_router)
app.include_router(normalization_router)
app.include_router(ai_router)
app.include_router(risk_router)
app.include_router(policy_router)
app.include_router(analyze_router)