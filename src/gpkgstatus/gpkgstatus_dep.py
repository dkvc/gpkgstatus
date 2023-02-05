import argparse
import json
import os
import platform
import requests
import sys
import time

from termcolor import colored

@DeprecationWarning
def read_url(package_name: str, cache_file: str, version: str):
    url = f"https://bodhi.fedoraproject.org/updates/?search={package_name}"
    
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(colored("Error: Could not connect to bodhi.fedoraproject.org. Please check your internet connection.", "red"))
        sys.exit(1)
    
    if response.status_code == 200:
        data = json.loads(response.content)
        
        try:
            with open(cache_file, "w") as f:
                    json.dump(data, f)
        except PermissionError:
            print(colored("Error: Permission denied to access file. Please check the file permissions.", "red"))
            sys.exit(1)
        
        update_info = []
        if version:
            for update in data['updates']:
                if update['title'].endswith(version):
                    update_info = update
                    break
        else:
            for update in data['updates']:
                if len(update_info) >= 5:
                    break
                
                update_info.append(update)
    else:
        # package not found
        print(f"Package '{package_name}' not found on bodhi.fedoraproject.org")
        sys.exit(1)
        
    if update_info:
        print_info(update_info)

@DeprecationWarning
def read_file(cache_file: str, version: str):
    try:
        with open(cache_file, "r") as f:
                data = json.load(f)
                update_info = []
                if version:
                    for update in data['updates']:
                        if update['title'].endswith(version):
                            update_info = update
                            break
                else:
                    for update in data['updates']:
                        if len(update_info) >= 5:
                            break
                            
                        update_info.append(update)
    except PermissionError:
        print(colored("Error: Permission denied to access file. Please check the file permissions.", "red"))
        sys.exit(1)
                    
    print(colored("[Cached Data (less than 30 minutes ago)]", "red", attrs=["bold"]))
    print_info(update_info)

@DeprecationWarning
def print_info(update_info):
    colors = {"stable": "green",
              "testing": "yellow",
              "pending": "red"}
              
    if isinstance(update_info, dict):
        if update_info['status'] in colors:
            status_color = colors[update_info['status']]
        else:
            status_color = "blue"
            
        print_update_info(update_info, status_color)
        
    else:
        for update in update_info:
            if update['status'] in colors:
                status_color = colors[update['status']]
            else:
                status_color = "blue"

            print_update_info(update, status_color)
            

@DeprecationWarning
def main(args: argparse.Namespace):
    package_name = args.name
    version = args.distro_version
    force = args.force
    cache_file = f"{package_name}.json"
    cache_time = 1800
    
    if force:
        read_url(package_name, cache_file, version)
    else:
        if os.path.isfile(cache_file) and (time.time() - os.path.getmtime(cache_file) < cache_time):
            read_file(cache_file, version)
        else:
            read_url(package_name, cache_file, version)
