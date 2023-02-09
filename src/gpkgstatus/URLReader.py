import json
import requests

from os.path import join
from sys import exit
from tempfile import gettempdir
from termcolor import colored


class URLReader:
    class _StatusException(Exception):
        pass

    _url: str = ""

    def __init__(self, _url: str):
        try:
            response = requests.head(_url)

            if response.status_code != 200:
                print(
                    colored("Error: Website isn't returning HTTP Status Code (200 OK)")
                )
                raise URLReader._StatusException()

            self._url = _url

        except requests.ConnectionError:
            print(colored(f"Error: Could not connect to {_url}", "red"))
            exit(1)

    def __load_json(self):
        try:
            response = requests.get(self._url)
            return response.json()
        except:
            print(
                colored(
                    "Error: There is an issue parsing JSON from corresponding website. Check if given URL is website JSON URL",
                    "red",
                )
            )
            exit(1)

    def save_as_file(self, filename: str, data: str = None):
        if data is None:
            data = self.__load_json()

        temp_file = join(gettempdir(), filename)

        try:
            with open(temp_file, "w") as file:
                json.dump(data, file, skipkeys=True, indent=4)
        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check temp directory permissions.",
                    "red",
                )
            )
            exit(1)
