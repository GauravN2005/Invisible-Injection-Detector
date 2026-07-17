from app.ai.keywords import PROMPT_INJECTION_KEYWORDS


class RuleBasedDetector:

    @staticmethod
    def detect(text: str):

        text = text.lower()

        detected = []

        for keyword in PROMPT_INJECTION_KEYWORDS:

            if keyword in text:
                detected.append(keyword)

        return detected


class PromptInjectionDetector(RuleBasedDetector):
    pass