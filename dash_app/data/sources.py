import pathlib
import logging

import pandas as pd

# TODO setup proper logger
logger = logging.Logger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler())

DATASET_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
LOCAL_ADDRESS = pathlib.Path(".") / "spacex_launch_dash.csv"

LOADING_OPTIONS = {
    "DEFAULT": DATASET_URL,
    "ONLINE": DATASET_URL,
    "LOCAL": LOCAL_ADDRESS,
}


class DataReachabilityException(Exception):
    def __init__(self, msg: str | None = None):
        if msg:
            self.msg = msg
            return
        self.msg = ""

    def __repr__(self) -> str:
        return self.msg


def test_data_source(loading_option: str):
    try:
        pd.read_csv(LOADING_OPTIONS[loading_option])
        code = 1
    except Exception as e:
        msg = f"{loading_option = } - failed"
        msg2 = f"Data not found at {LOADING_OPTIONS[loading_option]}"
        message = "\n".join([msg, msg2])
        logger.exception(message)
        logger.exception(e)
        code = 0
        # Recursion ... to loop all the other sources
    return code


def get_data(loading_option: str = "ONLINE"):
    assert loading_option in LOADING_OPTIONS, KeyError("Loading option not recogniced")
    # Given option
    code = test_data_source(loading_option=loading_option)
    if code == 1:
        pd.read_csv(LOADING_OPTIONS[loading_option])

    # Rest of options
    other_options = list(LOADING_OPTIONS.keys())
    other_options.pop(other_options.index(loading_option))
    for option in other_options:
        code = test_data_source(option)
        if code == 1:
            return pd.read_csv(LOADING_OPTIONS[option])

    raise DataReachabilityException("No valid source found for data")


def extend_data(df: pd.DataFrame):
    assert (
        "Booster Version" in df
    ), "No 'Booster Version' column found. Failed data extension."

    # Given the booster version string shape ...

    df["Short version"] = [el.split()[1] for el in df["Booster Version"].tolist()]
    return df
