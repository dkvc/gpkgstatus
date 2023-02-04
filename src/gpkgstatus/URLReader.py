import json
import requests
import tempfile

from os.path import join
from sys import exit
from termcolor import colored


class URLReader:
    def __init__(self, url: str):
        try:
            response = requests.head(url)
            
            if response.status_code != 200:
                print(colored("Error: Website isn't returning HTTP Status Code (200 OK)"))
                exit(1)

        except requests.ConnectionError:
            print(colored("Error: Could not connect to {url}", "red"))
            exit(1)
    
    def _load_json(self):
        response = requests.get(self.url)
        return response.json()

    def save_as_file(self, filename: str, data: str=_load_json()):
        temp_file = join(tempfile.gettempdir(), filename)
        
        try:
            with open(temp_file, 'w') as file:
                json.dump(data, file,
                        skipkeys=True,
                        indent=4)
        except PermissionError:
            print(colored("Error: Permission denied. Please check temp directory permissions.", "red"))
            exit(1)