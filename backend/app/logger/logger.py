import logging
import os

from app.logger.formatter import get_formatter


LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "app.log")


if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)


logger = logging.getLogger("InvisibleInjectionDetector")

logger.setLevel(logging.INFO)

logger.handlers.clear()


file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setFormatter(get_formatter())

logger.addHandler(file_handler)