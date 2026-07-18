from app.ai.detector import PromptInjectionDetector
from app.ai.model import AIModel


class AIService:

    @staticmethod
    def analyze(text: str):

        matches = PromptInjectionDetector.detect(text)

        result = AIModel.predict(matches)

        return {
            "prediction": result["prediction"],
            "prediction_confidence": result["prediction_confidence"],
            "attack_probability": result["attack_probability"],
            "matches": matches
        }