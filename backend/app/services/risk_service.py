from app.risk.calculator import RiskCalculator


class RiskService:

    @staticmethod
    def evaluate(ai_result: dict):

        attack_probability = ai_result["attack_probability"]

        matches = ai_result["matches"]

        risk_score = RiskCalculator.calculate(
            attack_probability,
            matches
        )

        severity = RiskCalculator.severity(
            risk_score
        )

        return {
            "risk_score": risk_score,
            "severity": severity
        }