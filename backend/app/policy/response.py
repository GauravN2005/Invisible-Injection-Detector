from app.policy.policy import Policy


class PolicyResponse:

    @staticmethod
    def build(risk_result):

        action = Policy.decide(
            risk_result["risk_score"]
        )

        return {

            "risk_score": risk_result["risk_score"],

            "severity": risk_result["severity"],

            "action": action
        }