import os

from json import load as jsonload
from pathlib import Path
from sys import exit
from tempfile import gettempdir
from termcolor import colored
from time import time

class JSONFileReader:
    
    _keys: list = []
    _path: Path = Path()

    def __init__(self, _path: Path | str, *_keys):
        if len(_keys) < 1:
            print(colored("Error: At least one key is required"))
            exit(1)
        
        if not isinstance(_path, Path):
            _path = Path(os.path.join(gettempdir(), _path))
        
        if not (_path.exists() and _path.is_file()):
            print(colored("Error: Given Path either doesn't exist or is not a file"))
            exit(1)

        self._keys = list(_keys)
        self._path = _path
    
    def read(self, limit: int=5):
        try:
            with open(self._path, 'r') as file:
                data = jsonload(file)
                searched_info = []

                for key in self._keys:
                    if key not in data.keys:
                        print(colored(f"Warning: Key {key} doesn't exist"))
                    else:
                        for value in data[key]:
                            if len(searched_info) >= limit:
                                return searched_info
                            
                            searched_info.append(value)
        except PermissionError:
            print(colored("Error: Permission denied. Please check temp directory permissions.", "red"))
            exit(1)

    def relative_time(self):
        return time.time() - os.path.getmtime(self._path)