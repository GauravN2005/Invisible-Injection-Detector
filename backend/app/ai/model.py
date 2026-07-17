class AIModel:

    @staticmethod
    def predict(matches):

        if len(matches) == 0:

            return {

                "prediction": "Safe",

                "confidence": 0.95

            }

        return {

            "prediction": "Prompt Injection",

            "confidence": min(0.5 + len(matches) * 0.05, 0.99)

        }