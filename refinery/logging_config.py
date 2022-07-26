import logging.config
from pythonjsonlogger import jsonlogger

LOGGING_CONFIG = {
    "version": 1,
    # don't disable existing loggers to not silently swallow errors
    "disable_existing_loggers": False,
    "formatters": {
        # name can be anything
        "default": {
            "format": "%(asctime)s:%(name)s:%(lineno)d " "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(asctime)s [%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "json": {
            "class": "refinery.logging_config.ProgramJsonFormatter",
            "format": """
                    asctime: %(asctime)s
                    created: %(created)f
                    filename: %(filename)s
                    funcName: %(funcName)s
                    levelname: %(levelname)s
                    levelno: %(levelno)s
                    lineno: %(lineno)d
                    message: %(message)s
                    module: %(module)s
                    msec: %(msecs)d
                    name: %(name)s
                    pathname: %(pathname)s
                    process: %(process)d
                    processName: %(processName)s
                    relativeCreated: %(relativeCreated)d
                    thread: %(thread)d
                    threadName: %(threadName)s
                    exc_info: %(exc_info)s
                """,
            "datefmt": "%Y-%m-%d %H:%M:%S",  # How to display dates
        }
    },
    "handlers": {
        # names can be anything
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": "program.log.json",
            "formatter": "json",
            "maxBytes": 10 * 1024 * 1024,  # 10 MB
            "backupCount": 5,
            "mode": "a"  # append to log on restart
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file", "console"]
    }
}


class ProgramJsonFormatter(jsonlogger.JsonFormatter):
    program: str

    def process_log_record(self, log_record):
        log_record["program"] = self.program
        return log_record


def setup_logging(program_name: str):
    """
    :param program_name: used to name the log file and add attribute to json log records
    """
    LOGGING_CONFIG["handlers"]["file"]["filename"] = f"{program_name}.log.json"
    logging.config.dictConfig(LOGGING_CONFIG)
    for handler in logging.getLogger("").handlers:
        if isinstance(handler.formatter, ProgramJsonFormatter):
            handler.formatter.program = program_name
