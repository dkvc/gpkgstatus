import argparse

from JSONFileReader import JSONFileReader, FileNotFoundException
from URLReader import URLReader
from termcolor import colored

def select_url(name: str, version: int=None):
    first_letter = version[0]
    urls = {
        "f": f"https://bodhi.fedoraproject.org/updates/?search={name}",
    }

    if first_letter in urls:
        url = urls[first_letter]
    else:
        print(colored(f"Error: Invalid Distribution", "red"))
        exit(1)
    
    if len(version) > 1:
        url += f"&releases={version}"
    return url

def print_update_info(update: dict, status_color: str):
    colors = {"stable": "green",
              "testing": "yellow",
              "pending": "red"}
    
    if update['status'].lower() in colors:
        status_color = colors[update['status']]
    else:
        status_color = "blue"
    
    print(colored(f"Update ID: {update['updateid']}", status_color))
    print(colored(f"Package Name: {update['title']}", status_color))
    print(colored(f"Status: {update['status']}", status_color))
    print("------------------------------")

def main(args: dict):
    cache_time = 3600 # 1 hr

    if args["distro_version"]:
        cache_file = f"{args['name']}_{args['distro_version']}.json"
    else:
        cache_file = f"{args['name']}.json"

    url = select_url(args['name'], args['distro_version'].lower())
    
    try:
        file_reader = JSONFileReader(cache_file, "updates")
        
        if (args['force'] or \
            (file_reader.relative_time() > cache_time)):
            url_reader = URLReader(url)
            url_reader.save_as_file(cache_file)

    except FileNotFoundException:
        url_reader = URLReader(url)
        url_reader.save_as_file(cache_file)
        file_reader = JSONFileReader(cache_file, "updates")
        
    finally:
        updates = file_reader.read()
        
        if not updates:
            print(colored("No Updates Found. Check your arguments.", "red"))
            exit(0)

        for update in updates:
            print_update_info(update, "green")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "gpkgstatus",
        description= "Get Current Package Status from Fedora Updates System",
        usage = "gpkgstatus [-dv DISTRO_VERSION] name"
    )

    parser.add_argument('name', help='Name of the package')
    dv = parser.add_argument('-d', '--distro-version', help='Checks package status for corresponding Fedora version', default="f")
    parser.add_argument('-f', '--force', help="Sync cached info with Fedora Updates System", action='store_true')
    parser.add_argument('-v', '--version', help='Returns gpkgstatus version', action='version', version='0.5 (beta)')
    args = parser.parse_args()
    
    main(vars(args))