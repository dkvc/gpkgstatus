import argparse
import json
import os
import platform
import requests
import sys
import time

from termcolor import colored


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
            

def print_update_info(update: dict, status_color: str):
    print(colored(f"Update ID: {update['updateid']}", status_color))
    print(colored(f"Package Name: {update['title']}", status_color))
    print(colored(f"Status: {update['status']}", status_color))
    print("------------------------------")


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = "gpkgstatus",
                    description = "Get Current Package Status from Fedora Updates System",
                    usage="gpkgstatus [-d DISTRO_VERSION] name")

    parser.add_argument('name', help='Name of the package')
    parser.add_argument('-d', '--distro-version', help='Checks package status for corresponding Fedora version')
    parser.add_argument('-f', '--force', help="Sync cached info with Fedora Updates System", action='store_true')
    parser.add_argument('-v', '--version', help='Returns gpkgstatus version', action='version', version='0.4 (beta)')
    args = parser.parse_args()
    
    main(args)
