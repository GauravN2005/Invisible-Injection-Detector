from app.risk.scorer import RiskScorer


class RiskService:

    @staticmethod
    def evaluate(ai_result):

        confidence = ai_result["confidence"]

        matches = ai_result["matches"]

        return RiskScorer.score(
            confidence,
            matches
        )