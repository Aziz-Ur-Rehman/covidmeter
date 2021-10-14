"""
report_file_reader module reads daily reports from a csv file
and returns a list containg dictionaries of records.
"""

import errno
import os
from csv import DictReader


def load_reports_file(file_path: str) -> list[dict]:
    """
    Reads csv file and load covid records in a list of dicts

    @param file_path: path of csv file
    @return: covid records in a list of dicts
    @raise: This function doesn't raise any exception.
    """
    try:
        csv_dict_reader = DictReader(open(file_path, "r"))
    except FileNotFoundError:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)

    return list(csv_dict_reader)
