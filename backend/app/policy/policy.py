from app.policy.actions import PolicyAction


class Policy:

    @staticmethod
    def decide(score: float):

        if score < 30:
            return PolicyAction.ALLOW

        elif score < 70:
            return PolicyAction.WARN

        else:
            return PolicyAction.BLOCK