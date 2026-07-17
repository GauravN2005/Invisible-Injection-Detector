from app.ai.predictor import Predictor


class AIService:

    @staticmethod
    def analyze(text: str):

        return Predictor.analyze(text)