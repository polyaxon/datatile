import logging

from polyaxon import settings
from polyaxon.client.handlers.handler import PolyaxonHandler

EXCLUDE_DEFAULT_LOGGERS = ("polyaxon.client", "polyaxon.cli")


def setup_logging(send_logs, exclude=EXCLUDE_DEFAULT_LOGGERS):
    if settings.CLIENT_CONFIG.is_managed:
        return

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if PolyaxonHandler in map(type, logger.handlers):
        for handler in logger.handlers:
            if isinstance(handler, PolyaxonHandler):
                handler.set_send_logs(send_logs=send_logs)
    else:
        handler = PolyaxonHandler(send_logs=send_logs)

    logger.addHandler(handler)

    for logger_name in exclude:
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        logger.addHandler(logging.StreamHandler())
