"""A Config module that creates, reads and checks ~/.gpkgconfig JSON \
    config file.
"""

import logging
import sys

from pathlib import Path

import json
import pyinputplus as pyinp

from termcolor import colored


class Config:
    """A Config class that contains information about fields \
        or keys of the config file.

        It contains getters for `cache_time` and `verbose`. In
        case if `cache_time` or `verbose` is not determined, the default
        values (`52 min`) and (`False`) are set respectively.
    """

    _cache_time: int
    _path: Path
    _verbose: bool

    # _cache_time = 52 min (default)
    # _verbose = False (default)
    def __init__(self, _cache_time: int = 52 * 60, _verbose: bool = False):
        self._cache_time = _cache_time
        logging.info("Set Cache Time: %d min", _cache_time // 60)

        self._path = Path.expanduser(Path("~/.gpkgconfig"))
        self._verbose = _verbose

    def user_input(self):
        """Sets the fields based on user input.

        Using `PyInputPlus` library for safe input, the input for
        `cache_time` and `verbose` are set accordingly.
        """

        print(colored("Creating a new config file...", "green"))

        _cache_time = pyinp.inputNum(
            colored("Cache Time (min/[default]): ", "yellow"), blank=True
        )

        if _cache_time:
            self._cache_time = _cache_time * 60
        else:
            logging.info("Default Cache Time: %d min", self._cache_time // 60)

        _verbose = pyinp.inputYesNo(
            colored("Do you want verbose info (y/n[default]): ", "yellow"), blank=True
        )
        if _verbose:
            self._verbose = _verbose == "yes"
        else:
            logging.info("Default Verbose Value: %r", self._verbose)

    def _check(self) -> bool:
        """Checks whether config file exists, and also checks if \
            it is a valid JSON file.

            In case if file doesn't exist, it automatically creates
            a config file based on user input.

        Returns:
            bool: Whether config file exists or not
        """
        _path = self._path
        if not (_path.exists() and _path.is_file):
            print(colored("Config file doesn't exist.", "light_red"))
            self.user_input()
            self.create()

        try:
            with open(_path, encoding="utf-8") as file:
                json.load(file)
        except json.JSONDecodeError:
            print(colored("File is not a valid JSON file.", "light_red"))
            return False

        logging.info("Config file exists")
        return True

    def create(self):
        """Creates the JSON config (~/.gpkgconfig) file.

        Based on the given fields, the JSON config file is created.
        If user home directory is permissive, the method will ask to
        check home directory permissions.
        """

        config = {"cache_time": self._cache_time, "verbose": self._verbose}
        try:
            with open(self._path, "w", encoding="utf-8") as file:
                json.dump(config, file, skipkeys=True, indent=4)

            logging.info("Config File written to %s", str(self._path))

        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check home directory permissions.",
                    "red",
                )
            )
            sys.exit(1)

    def read(self):
        """Reads the JSON config file

        It also checks if (`cache_time` and `verbose`) are keys in
        JSON file. In case if one of them doesn't exist, it states
        that file is not a valid config file and asks the user
        for overwriting the file.
        """

        with open(self._path, encoding="utf-8") as file:
            data = json.load(file)

        if all(key not in data.keys() for key in ("cache_time", "verbose")):
            print(colored("File is not a valid Config file.", "light_red"))
            self.overwrite()
            logging.info("File overwritten.")

        self._cache_time = data["cache_time"]
        self._verbose = data["verbose"]

    def overwrite(self):
        """Asks the user for overwriting config file."""

        _overwrite = pyinp.inputYesNo(
            colored("Do you want to overwrite the file (y/n[default]): ", "yellow"),
            blank=True,
        )
        if not _overwrite or _overwrite == "no":
            sys.exit(1)
        else:
            self.user_input()
            self.create()
            logging.info("File overwritten.")

    def set_info(self):
        """The main program that checks the file using `_check()`
        function.

        If output of checking is False, it starts to overwrite
        the invalid file, or else, it reads the file.
        """

        if not self._check():
            self.overwrite()

        self.read()

    def get_cache_time(self) -> int:
        """Getter for field `_cache_time`

        Returns:
            int: Value of `_cache_time`
        """

        return self._cache_time

    def get_verbose_status(self) -> bool:
        """Getter for field `_verbose`

        Returns:
            bool: Value of `_verbose`
        """
        return self._verbose
