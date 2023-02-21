"""The gpkgstatus module searches package and prints its update info.

The gpkgstatus module that searches the package from selected url or
cached file and prints the update info to terminal.

"""
import argparse
import logging
import sys

from typing import Optional

from termcolor import colored

from gpkgstatus.utils.json_file_reader import FileNotFoundException, JSONFileReader
from gpkgstatus.utils.url_reader import URLReader
from gpkgstatus import __version__


def select_url(name: Optional[str], version: str):
    """Selects url based on name based on corresponding release \
        version if specified or else globally.

    Selects url based on first character of version from a dictionary of
    urls. If url is not present in urls, then program halts with exit
    status 1 and immediately states that given version/Linux distribution
    release is invalid.

    Args:
        name (Optional[str]): Name of the package. Defaults to None if none \
            is given in command-line arguments.
        version (str): If version is given, then package will be searched \
            in specific release; or else the package will be searched globally. \
                Defaults to None.

    Returns:
        str : Complete URL containing parameters based on given arguments that searches \
            a package with given name in corresponding release version if specified.
    """
    first_letter = version[0]
    urls = {
        "f": "https://bodhi.fedoraproject.org/updates/?",
    }

    if first_letter in urls:
        url = urls[first_letter]
        logging.info("Given version is in list")
    else:
        print(colored("Error: Invalid Distribution Release. Format: f{version}", "red"))
        sys.exit(1)

    if name:
        url += f"&search={name}"

    if len(version) > 1:
        url += f"&releases={version}"

    logging.info("URL Selected: %s", url)

    return url


def print_update_info(update: dict, status_color: str):
    """Prints colored update info to terminal.

    The color is selected based on current status of package
    from a colors dictionary with keys as status and colors
    as values. If status is not present in colors, then
    default color is blue.

    If terminal does not support ASCII colors, then normal text
    is printed.

    Args:
        update (dict): Dictionary of Updates containing metadata.
        status_color (str): ASCII Color if explicitly given.
    """
    colors = {"stable": "green", "testing": "yellow", "pending": "red"}

    if update["status"].lower() in colors:
        status_color = colors[update["status"]]
    else:
        status_color = "blue"

    print(colored(f"Update ID: {update['updateid']}", status_color))
    print(colored(f"Package Name: {update['title']}", status_color))
    print(colored(f"Status: {update['status']}", status_color))
    print("------------------------------")


def search_pkg(args: dict):
    """Search Package from cached file or given JSON url.

    If --force argument is specified, url will be used for searching
    irrespective of whether cached expired or not. After requesting the
    url, the program stores the JSON response in a file named as
    "name_release.json"; that has searched packages of corresponding release.
    In case if --name argument is not specified, the file will be named
    as "None_release.json".

    Args:
        args (dict): Command-Line arguments in the form of dictionary.
    """
    if args["verbose"]:
        logging.basicConfig(level=logging.INFO)

    cache_time = 3600  # 1 hr
    release = args["release"][0]
    name = args["name"] if args["name"] else None

    try:
        limit = int(args["limit"][0])
    except ValueError:
        print(colored("You must enter an integer value.", "red"))
        sys.exit(1)

    cache_file = f"{name}_{release}.json"
    url = select_url(name, release.lower())

    try:
        file_reader = JSONFileReader(cache_file, "updates")

        if args["force"]:
            logging.info("Forced to update the cache")

        if args["force"] or (file_reader.relative_time() > cache_time):
            logging.info("File cache is outdated")
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
            sys.exit(0)

        for update in updates:
            print_update_info(update, "green")


def cli():
    """Command Line Interface of Program.

    The CLI takes arguments from terminal ,parses it using ArgumentParser,
    converts arguments into form of dictionary, and calls the search_pkg
    function.
    """
    parser = argparse.ArgumentParser(
        prog="gpkgstatus",
        description="Get Current Package Status from Fedora Updates System",
    )

    parser.add_argument(
        "-n",
        "--name",
        help="Name of the package",
        type=str,
        nargs=1,
    )
    parser.add_argument(
        "-r",
        "--release",
        help="Checks package status for corresponding Fedora release",
        default="f",
        nargs=1,
    )
    parser.add_argument(
        "-f",
        "--force",
        help="Sync cached info with Fedora Updates System",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--limit",
        help="Maximum limit on number of packages shown for package search",
        default="5",
        nargs=1,
    )
    parser.add_argument(
        "-v", "--verbose", help="Enable verbose output", action="store_true"
    )
    parser.add_argument(
        "--version",
        help="gpkgstatus version",
        action="version",
        version=__version__,
    )
    args = parser.parse_args()

    search_pkg(vars(args))
