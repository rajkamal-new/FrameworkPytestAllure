import inspect
import logging
import os


def get_logger():
    logger = logging.getLogger(inspect.stack()[1][3])
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    if not logger.handlers:

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(
            os.path.join(os.path.dirname(__file__), "..","target", "logs", "test_log.log"),
            mode='a')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# logger object
# formatter
# set level
# fh = logging.FileHandler(filepath, mode)
# fh.setFormatter, fh.setLevel
# logger.addHandler(fh)