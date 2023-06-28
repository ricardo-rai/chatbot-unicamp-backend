import json
import logging
import traceback
from socket import gethostname

from config import settings


class Logger:
    def setup_logging():
        log_level = settings.get("LOG_LEVEL")
        local_execution = settings.get("LOCAL_EXECUTION")

        logger = logging.getLogger()
        logger.setLevel(log_level)

        handler = logging.StreamHandler()
        if local_execution:
            msg_format = "%(asctime)s|%(levelname)s - %(module)s - %(message)s"
            handler.setFormatter(logging.Formatter(msg_format))
        else:
            handler.setFormatter(JSONFormatter())

        logger.addHandler(handler)


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        record.msg = {
            "timestamp": record.created,
            "_log_type": "application",
            "_application": settings.get("APPLICATION"),
            "_environment": settings.get("ENV_FOR_DYNACONF"),
            "host": gethostname(),
            "level": record.levelname,
            "message": str(record.msg),
        }

        if record.levelname == "ERROR":
            record.msg["_stack_trace"] = traceback.format_exc()

        for attr in vars(record):
            if attr[0] == "_":
                record.msg[attr] = getattr(record, attr)

        record.msg = json.dumps(record.msg)
        return super().format(record)
