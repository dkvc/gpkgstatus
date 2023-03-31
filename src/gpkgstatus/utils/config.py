"""A Config module that creates, reads and checks ~/.gpkgconfig JSON \
    config file.
"""

import json
import logging
import os
import sys

from pathlib import Path
from random import randint

from termcolor import colored


class Config:
    """A Config class that contains fields or keys of the \
        config file.
    """

    cache_time: int
    verbose: bool
    __path: Path

    def __init__(self):
        self.cache_time = randint(52, 65) * 60
        self.verbose = False

        logging.info("Set Cache Time: %d min", self.cache_time // 60)
        logging.info("Set Verbose to %s", self.verbose)

        # Set Path
        if "XDG_CONFIG_HOME" in os.environ:
            self.__path = Path(os.environ["XDG_CONFIG_HOME"]).joinpath(".gpkgconfig")
        else:
            self.__path = Path.expanduser(Path("~/.config/.gpkgconfig"))

        logging.info("Set path to %s", self.__path)

    def check(self) -> bool:
        """Checks whether config file exists, and also checks if \
            it is a valid JSON file.

        Returns:
            bool: Whether config file exists and is a valid JSON file
        """
        path = self.__path
        if not (path.exists() and path.is_file()):
            logging.info("Config file not found")
            return False

        try:
            with open(path, encoding="utf-8") as file:
                json.load(file)
        except json.JSONDecodeError:
            logging.info("Config file is not a valid JSON file")
            return False

        logging.info("Config file is valid")
        return True

    def create(self):
        """Creates config file in corresponding path.

        If script doesn't have permissions to write to config dir,
        it will tell the user to check config dir permissions.
        """

        config = {"cache_time": self.cache_time, "verbose": self.verbose}
        try:
            with open(self.__path, "w", encoding="utf-8") as file:
                json.dump(config, file, skipkeys=True, indent=4)

            logging.info("Config file written to %s", self.__path)

        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check home directory permissions.",
                    "red",
                )
            )
            sys.exit(1)

    def read(self):
        """If config file exists, this method reads the JSON config file.

        It also checks if ("cache_time", "verbose") are keys in JSON file.
        In case if one of them doesn't exist, it states that file is not
        a valid config file.
        """
        with open(self.__path, encoding="utf-8") as file:
            data = json.load(file)

        if all(key not in data.keys() for key in ("cache_time", "verbose")):
            print(colored("File is not a valid Config file.", "light_red"))
            sys.exit(1)

        self.cache_time = data["cache_time"]
        self.verbose = data["verbose"]

    def main(self):
        """Main Method

        The method checks if file exists and reads the file. If file
        is not generated, then it calls the `create()` function.
        """
        if not self.check():
            self.create()

        self.read()
