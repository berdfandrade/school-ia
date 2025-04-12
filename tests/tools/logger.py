import logging

logger = logging.getLogger(__name__)

def it(description):
    def wrapper(func):
        logger.info(description)
        return func
    return wrapper

