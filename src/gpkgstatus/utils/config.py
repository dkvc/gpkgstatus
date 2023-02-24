import logging
import sys

from pathlib import Path

import json
import pyinputplus as pyinp

from termcolor import colored

class Config:
    _cache_time: int
    _path: Path
    _verbose: bool
    
    def __init__(self, _cache_time: int, _verbose: bool):
        self._cache_time = _cache_time
        logging.info(f"Set Cache Time: {_cache_time // 60}")
        
        self._path = Path.expanduser(Path("~/.gpkgconfig"))
        self._verbose = _verbose

    def user_input(self):
        print(
            colored(
                "Creating a new config file...",
                "green"
            )
        )

        _cache_time = pyinp.inputNum(colored("Cache Time (min/[default]): ", "yellow"), blank=True)
        if _cache_time:
            self._cache_time = _cache_time
        else:
            # 52 min (default)
            self._cache_time = 52 * 60
        
        _verbose = pyinp.inputYesNo(colored("Do you want verbose info (y/n[default]): ", "yellow"), blank=True)
        if _verbose:
            self._verbose = False if _verbose == "no" else True
        else:
            # No verbose (default)
            self._verbose = False 


    def _check(self):
        _path = self._path
        if not (_path.exists() and _path.is_file):
            print(
                colored(
                    "Config file doesn't exist."
                    "light_red"
                )
            )
            self.user_input()
        
        try:
            with open(_path, encoding="utf-8") as file:
                json.load(file)
        except json.JSONDecodeError:
            print(
                colored(
                    "File is not a valid JSON file."
                    "light_red"
                )
            )
            return False

        logging.info("Config file exists")
        return True

        
    def create(self):
        config = {"cache_time": self._cache_time,
                    "verbose":self._verbose}
        try:
            with open(self._path, "w", encoding="utf-8") as file:
                json.dump(config, self._path, skipkeys=True, indent=4)

            logging.info("Config File written")

        except PermissionError:
            print(
                colored(
                    "Error: Permission denied. Please check temp directory permissions.",
                    "red",
                )
            )
            sys.exit(1)

    def read(self):
        with open(self._path, encoding="utf-8") as file:
            data = json.load(file)
        
        if ("cache_time", "verbose") not in data.keys():
            print(
                colored(
                    "File is not a valid Config file."
                    "light_red"
                )
            )
            self.overwrite()
            logging.info("File overwritten.")

        
        self._cache_time = data["cache_time"]
        self._verbose = data["verbose"]

    def overwrite(self):
        _overwrite = pyinp.inputYesNo(colored("Do you want to overwrite the file (y/n[default]): ", "yellow"), blank=True)
        if not _overwrite or _overwrite == "no":
            exit(1)
        else:
            self.user_input()
            self.create()
            logging.info("File overwritten.")

    def set_info(self):
        if not self._check():
            self.overwrite()
        
        self.read()

    def get_cache_time(self):
        return self._cache_time
        
    def get_verbose_status(self):
        return self._verbose