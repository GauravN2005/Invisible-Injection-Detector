from app.risk.calculator import RiskCalculator
from app.risk.severity import Severity


class RiskScorer:

    @staticmethod
    def score(confidence, matches):

        risk_score = RiskCalculator.calculate(
            confidence,
            matches
        )

        if risk_score < 30:
            severity = Severity.LOW

        elif risk_score < 60:
            severity = Severity.MEDIUM

        elif risk_score < 85:
            severity = Severity.HIGH

        else:
            severity = Severity.CRITICAL

        return {
            "risk_score": risk_score,
            "severity": severity
        }