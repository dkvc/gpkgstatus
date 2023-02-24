import logging
import sys

from pathlib import Path

import json

from termcolor import colored

class Config:
    _cache_time: int
    _path: Path
    _verbose: bool
    
    # _cache_time = 52 min
    def __init__(self, _verbose: bool=False, _cache_time: int=52*60):
        self._cache_time = _cache_time
        logging.info(f"Set Cache Time: {_cache_time // 60}")
        
        self._path = Path.expanduser(Path("~/.gpkgconfig"))
        self._verbose = _verbose

    def _check(self):
        _path = self._path
        if not (_path.exists() and _path.is_file):
            print(
                colored(
                    "Config file doesn't exist."
                    "light_red"
                )
            )
            return False
        
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