from app.policy.response import PolicyResponse


class PolicyEvaluator:

    @staticmethod
    def evaluate(risk_result):

        return PolicyResponse.build(risk_result)