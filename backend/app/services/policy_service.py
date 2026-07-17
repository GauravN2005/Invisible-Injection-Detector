from app.policy.evaluator import PolicyEvaluator


class PolicyService:

    @staticmethod
    def evaluate(risk_result):

        return PolicyEvaluator.evaluate(risk_result)