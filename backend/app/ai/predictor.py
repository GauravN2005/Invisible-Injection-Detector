from app.ai.detector import RuleBasedDetector
from app.ai.model import AIModel


class Predictor:

    @staticmethod
    def analyze(text: str):

        matches = RuleBasedDetector.detect(text)

        prediction = AIModel.predict(matches)

        prediction["matches"] = matches

        return prediction