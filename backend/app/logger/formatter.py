import logging


def get_formatter():

    return logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s",

        "%Y-%m-%d %H:%M:%S"

    )