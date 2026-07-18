from app.normalization.normalizer import InputNormalizer


class NormalizationService:

    @staticmethod
    def process(text: str) -> str:
        """
        Process and normalize user input.
        """

        normalized_text = InputNormalizer.normalize(text)

        return normalized_text