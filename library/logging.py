import logging


def create_stdout_logger(name: str, level=logging.DEBUG) -> logging.Logger:
    """Create a generic stdout logger with unique name and level if specified"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(ch)

    return logger