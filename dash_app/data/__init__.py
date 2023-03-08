import logging

from .sources import get_data, extend_data

# TODO setup proper logger
logger = logging.Logger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler())


class DataExtensionException(Exception):
    def __init__(self, msg: str | None = None):
        if msg:
            self.msg = msg
            return
        self.msg = ""

    def __repr__(self) -> str:
        return self.msg


DATASET = get_data()

try:
    df = extend_data(DATASET)
except AssertionError as e:
    logger.exception(e)
    raise DataExtensionException("Uncapabale of extensing data")
else:
    DATASET = df
