import logging
from refinery.environ import LOCAL_OUTPUT_DIR


def setup_logging():
    """Set up a logger object that will log files to file and to the console"""

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    log_file = f"{LOCAL_OUTPUT_DIR}/console_outputs.log"

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info(f"Logging to %s", log_file)

    return logger
