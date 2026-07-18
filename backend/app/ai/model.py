class AIModel:

    @staticmethod
    def predict(matches: list):

        # Safe input
        if len(matches) == 0:
            return {
                "prediction": "Safe",
                "prediction_confidence": 0.95,
                "attack_probability": 0.05
            }

        # Prompt Injection detected
        attack_probability = min(
            0.30 + (len(matches) * 0.15),
            0.99
        )

        prediction_confidence = attack_probability

        return {
            "prediction": "Prompt Injection",
            "prediction_confidence": round(prediction_confidence, 2),
            "attack_probability": round(attack_probability, 2)
        }