import logging.config

from virtualspace import settings


def setup_logging():
    logging.config.fileConfig(settings.LOGGING_INI_PATH, disable_existing_loggers=False)
