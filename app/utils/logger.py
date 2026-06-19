import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

if not logger.handlers:
    logger.addHandler(file_handler)