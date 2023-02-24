"""A JSON File Reader module that searches for given keys.

The module searches a JSON File from a given path for
specific keys and stores their values for further
processing or output.

Raises:
    FileNotFoundException: Manual Exception class that is raised if \
            file doesn't exist or given path is not a file path.

"""
import logging
import os
import sys

from json import load as jsonload
from pathlib import Path
from tempfile import gettempdir
from time import time
from typing import Union

from termcolor import colored


class FileNotFoundException(Exception):
    """Returns FileNotFoundException if file doesn't exist.

    This exception is created for manually raising exceptions
    if file doesn't exist or given path is not a file path.
    These exceptions are handled manually as group.
    """


class JSONFileReader:
    """A Custom JSON File Reader class created using requests package.

    The class is initialized by a JSON file path (which can be a Path object 
    or str) and a list of keys to be searched for.

    Raises:
        FileNotFoundException: Manual Exception class that is raised if \
            file doesn't exist or given path is not a file path.
    """

    _keys: list = []
    _path: Union[Path, str] = Path()

    def __init__(self, _path: Union[Path, str], *_keys):
        if len(_keys) < 1:
            print(colored("Error: At least one key is required"))
            sys.exit(1)

        if not isinstance(_path, Path):
            _path = Path(os.path.join(gettempdir(), _path))
            logging.info("Path created")

            logging.debug("Path created using filename")

        else:
            logging.debug("Path was directly given")

        if not (_path.exists() and _path.is_file()):
            raise FileNotFoundException()

        self._keys = list(_keys)
        self._path = _path

    def read(self, limit: int = 5):
        """Reads a JSON file and returns limit number of values from \
            corresponding keys.

        If one of the corresponding keys doesn't exist, the log warns
        that key doesn't exist.
        If PermissionError is raised, then the program halts with exit 
        status 1 and immediately states that permission is denied. 

        Args:
            limit (int, optional): Limit to number of values. Defaults to 5.

        Returns:
            List[Any] : Values for corresponding keys, i.e, information that
            was to searched for.
        """
        try:
            with open(self._path, "r", encoding="utf-8") as file:
                data = jsonload(file)
                logging.info("JSON loaded successfully from file")

                searched_info = []

                for key in self._keys:
                    if key not in data.keys():
                        logging.warning(colored(f"Warning: Key {key} doesn't exist"))
                    else:
                        for value in data[key]:
                            if len(searched_info) >= limit:
                                logging.info(
                                    "Package is searched and found some entries"
                                )
                                return searched_info

                            searched_info.append(value)

                logging.info("Package is searched but no entries found")

        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check temp directory permissions.",
                    "red",
                )
            )
            sys.exit(1)

        return searched_info

    def relative_time(self):
        """Returns the time difference between last modified time of given file and \
            current os time in seconds."""
        logging.debug("Relative time is determined")
        return time() - os.path.getmtime(self._path)
