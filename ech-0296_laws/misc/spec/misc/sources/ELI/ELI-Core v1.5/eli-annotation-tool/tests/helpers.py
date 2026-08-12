import contextlib
import logging

@contextlib.contextmanager
def silence_logging_warning():
    logging.disable(logging.WARNING)
    yield
    logging.disable(logging.NOTSET)
