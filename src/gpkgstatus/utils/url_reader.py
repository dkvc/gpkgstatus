"""A URL Reader module that reads a JSON url and saves its response \
    as a file in tempdir.

Raises:
    URLReader._StatusException: Manual exception raised if \
            HTTP status code is not OK (200).

"""
import json
import logging
import sys

from os.path import join
from tempfile import gettempdir
from time import sleep

import requests

from termcolor import colored


# pylint:disable=too-few-public-methods
class URLReader:
    """A Custom URL Reader class created using requests package.

    The class initializer uses a HEAD request to determine if given 
    JSON url exists.

    Raises:
        URLReader._StatusException: Manual exception raised if \
            HTTP status code is not OK (200).
    """

    class _StatusException(Exception):
        pass

    _url: str = ""

    def __init__(self, _url: str):
        try:
            response = requests.head(_url, timeout=15)

            if response.status_code != 200:
                print(
                    colored("Error: Website isn't returning HTTP Status Code (200 OK)")
                )
                raise URLReader._StatusException()

            self._url = _url
            logging.info("URL %s returned OK", _url)

        except requests.ConnectionError:
            print(colored(f"Error: Could not connect to {_url}", "red"))
            sys.exit(1)

    def _load_json(self):
        """Loads the given JSON url.

        If corresponding url is not a JSON url or if JSON decoding fails, then
        the program halts with exit status 1 and immediately states that
        there is an issue parsing JSON from corresponding url and might
        not be a valid JSON url.

        Returns:
            Any: Returns JSON response of corresponding JSON url.
        """
        try:
            response = requests.get(self._url, timeout=15)
            sleep(1)
            logging.info("GET Request from %s succeeded", self._url)

            return response.json()
        except requests.exceptions.JSONDecodeError:
            print(
                colored(
                    "Error: There is an issue parsing JSON from corresponding website. \
                        Check if given URL is valid JSON URL",
                    "red",
                )
            )
            sys.exit(1)

    # pylint:disable=duplicate-code
    def save_as_file(self, filename: str, data: str = ""):
        """Saves JSON response in a file.

        If PermissionError is raised, then the program halts with exit
        status 1 and immediately states that permission is denied.

        Args:
            filename (str): Name of the file.
            data (str, optional): Corresponding JSON response/file.
            If no file is given, it takes JSON response as data from
            corresponding url.
        """
        if not data:
            data = self._load_json()
            logging.info("JSON loaded successfully from URL")

        temp_file = join(gettempdir(), filename)

        try:
            with open(temp_file, "w", encoding="utf-8") as file:
                json.dump(data, file, skipkeys=True, indent=4)

            logging.info("JSON stored in %s", filename)

        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check temp directory permissions.",
                    "red",
                )
            )
            sys.exit(1)
