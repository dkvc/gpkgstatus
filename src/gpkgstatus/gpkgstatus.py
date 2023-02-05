import argparse

from JSONFileReader import JSONFileReader, FileNotFoundException
from URLReader import URLReader
from termcolor import colored

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

def main(args: argparse.Namespace):
    args = vars(args)

    cache_file = f"{args['name']}.json"
    cache_time = 3600 # 1 hr

    if args['distro_version'].lower().startswith("f"):
        url = f"https://bodhi.fedoraproject.org/updates/?search={args['name']}"
    
    try:
        file_reader = JSONFileReader(cache_file, "updates", None)
        if (args['force'] or \
            (file_reader.relative_time() > cache_time)):
            url_reader = URLReader(url)
            url_reader.save_as_file(cache_file)
    except FileNotFoundException:
        url_reader = URLReader(url)
        url_reader.save_as_file(cache_file)
        file_reader = JSONFileReader(cache_file, "updates", None)
    finally:
        updates = file_reader.read()
        for update in updates:
            print_update_info(update, "green")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "gpkgstatus",
        description= "Get Current Package Status from Fedora Updates System",
        usage = "gpkgstatus [-dv DISTRO_VERSION] name"
    )

    parser.add_argument('name', help='Name of the package')
    dv = parser.add_argument('-d', '--distro-version', help='Checks package status for corresponding Fedora version')
    parser.add_argument('-f', '--force', help="Sync cached info with Fedora Updates System", action='store_true')
    parser.add_argument('-v', '--version', help='Returns gpkgstatus version', action='version', version='0.4 (beta)')
    args = parser.parse_args()

    if not args.distro_version.lower().startswith(("f", "o")):
        raise argparse.ArgumentError(dv , "Invalid Distro version")
    
    main(args)