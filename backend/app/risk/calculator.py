class RiskCalculator:

    @staticmethod
    def calculate(attack_probability: float, matches: list):

        score = attack_probability * 80

        score += len(matches) * 5

        score = min(score, 100)

        return round(score, 2)

    @staticmethod
    def severity(score: float):

        if score < 25:
            return "Low"

        elif score < 50:
            return "Medium"

        elif score < 75:
            return "High"

        else:
            return "Critical"