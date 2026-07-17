class RiskCalculator:

    @staticmethod
    def calculate(confidence: float, matches: list):

        score = 0

        # AI confidence contributes up to 70 points
        score += confidence * 70

        # Each keyword contributes 5 points
        score += len(matches) * 5

        # Cap the score
        score = min(score, 100)

        return round(score, 2)