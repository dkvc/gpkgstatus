from gpkgstatus.JSONFileReader import JSONFileReader, FileNotFoundException
from gpkgstatus.URLReader import URLReader
from termcolor import colored


def select_url(name: str, version: int = None):
    first_letter = version[0]
    urls = {
        "f": f"https://bodhi.fedoraproject.org/updates/?search={name}",
    }

    if first_letter in urls:
        url = urls[first_letter]
    else:
        print(colored("Error: Invalid Distribution. Format: f{version}", "red"))
        exit(1)

    if len(version) > 1:
        url += f"&releases={version}"
    return url


def print_update_info(update: dict, status_color: str):
    colors = {"stable": "green", "testing": "yellow", "pending": "red"}

    if update["status"].lower() in colors:
        status_color = colors[update["status"]]
    else:
        status_color = "blue"

    print(colored(f"Update ID: {update['updateid']}", status_color))
    print(colored(f"Package Name: {update['title']}", status_color))
    print(colored(f"Status: {update['status']}", status_color))
    print("------------------------------")


def main(args: dict):
    cache_time = 3600  # 1 hr
    distro_version = args["distro_version"][0]

    try:
        limit = int(args["limit"][0])
    except ValueError:
        print(colored("You must enter an integer value.", "red"))
        exit(0)

    cache_file = f"{args['name']}_{distro_version}.json"
    url = select_url(args["name"], distro_version.lower())

    try:
        file_reader = JSONFileReader(cache_file, "updates")

        if args["force"] or (file_reader.relative_time() > cache_time):
            url_reader = URLReader(url)
            url_reader.save_as_file(cache_file)

    except FileNotFoundException:
        url_reader = URLReader(url)
        url_reader.save_as_file(cache_file)
        file_reader = JSONFileReader(cache_file, "updates")

    finally:
        updates = file_reader.read(limit)

        if not updates:
            print(colored("No Updates Found. Check your arguments.", "red"))
            exit(0)

        for update in updates:
            print_update_info(update, "green")
