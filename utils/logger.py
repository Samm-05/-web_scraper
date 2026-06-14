from loguru import logger

logger.add(
    "logs/scraper.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO"
)

logger.info(
    "Logger initialized"
)