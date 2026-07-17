from app.services.extractor_service import ContentExtractor
from app.services.normalization_service import NormalizationService
from app.services.ai_service import AIService
from app.services.risk_service import RiskService
from app.services.policy_service import PolicyService

from app.logger.logger import logger


class AnalyzeService:

    @staticmethod
    def analyze(file_type: str, content: str):

        try:
            logger.info(f"Started Analysis | Type={file_type}")

            # Step 1: Content Extraction
            extracted_text = ContentExtractor.extract(
                content,
                file_type
            )

            logger.info("Extraction Completed")

            # Step 2: Input Normalization
            normalized_text = NormalizationService.process(
                extracted_text
            )

            logger.info("Normalization Completed")

            # Step 3: AI Detection
            ai_result = AIService.analyze(
                normalized_text
            )

            logger.info(
                f"Prediction={ai_result['prediction']} | "
                f"Confidence={ai_result['confidence']}"
            )

            # Step 4: Risk Scoring
            risk_result = RiskService.evaluate(
                ai_result
            )

            logger.info(
                f"Risk={risk_result['risk_score']} | "
                f"Severity={risk_result['severity']}"
            )

            # Step 5: Policy Decision
            policy_result = PolicyService.evaluate(
                risk_result
            )

            logger.info(
                f"Action={policy_result['action']}"
            )

            logger.info("Analysis Completed Successfully")

            return {
                "original_text": content,
                "extracted_text": extracted_text,
                "normalized_text": normalized_text,
                "prediction": ai_result["prediction"],
                "confidence": ai_result["confidence"],
                "matches": ai_result["matches"],
                "risk_score": risk_result["risk_score"],
                "severity": risk_result["severity"],
                "action": policy_result["action"]
            }

        except Exception as e:
            logger.exception(f"Analysis Failed: {str(e)}")
            raise