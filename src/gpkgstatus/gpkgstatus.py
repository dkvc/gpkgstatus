"""The gpkgstatus module searches package and prints its update info.

The gpkgstatus module that searches the package from selected url or
cached file and prints the update info to terminal.

"""
import argparse
import logging
import sys

from typing import Optional

from termcolor import colored

from gpkgstatus.utils.config import Config
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
        logging.debug("Invalid Version: %s", version)

        sys.exit(1)

    if name:
        url += f"&search={name}"

    if len(version) > 1:
        url += f"&releases={version}"

    logging.info("URL Selected: %s", url)

    return url


def print_update_info(update: dict, status_color: str = None, more_info=False):
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
    if more_info:
        print(colored(f"Alias: {update['alias']}", status_color))
        print(colored(f"Date Submitted: {update['date_submitted']}", status_color))
        print(colored(f"Severity: {update['severity']}", status_color))
        print(colored(f"Version Hash: {update['version_hash']}", status_color))
        print(colored(f"URL: {update['url']}", status_color))
        print(colored(f"Notes: {update['notes']}", status_color))

    print("------------------------------")


def search_pkg(args: dict):
    """Search Package from cached file or given JSON url.

    If --force argument is specified, url will be used for searching
    irrespective of whether cached expired or not. After requesting the
    url, the program stores the JSON response in a file named as
    "name_release.json"; that has searched packages of corresponding release.
    In case if --name argument is not specified, the file will be named
    as "None_release.json".

    If --noconfig argument is specified, config will be ignored and values of
    cache_time and verbose will be set to default values.

    Args:
        args (dict): Command-Line arguments in the form of dictionary.
    """
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler(sys.stdout))

    if not args["noconfig"]:
        config = Config()
        config.set_info()

        if config.get_verbose_status() or args["verbose"]:
            logger.setLevel(logging.INFO)

        cache_time = config.get_cache_time()
    else:
        # 52 min (default value)
        cache_time = 52 * 60
        if args["verbose"]:
            logger.setLevel(logging.INFO)

        logging.info("Forced to ignore config file")

    logging.info(args)
    logging.info("Cache Time: %d min", cache_time // 60)

    release = args["release"][0]
    name = args["name"][0] if args["name"] else None
    more_info = args["moreinfo"]

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
            print_update_info(update, more_info=more_info)


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
        "-f",
        "--force",
        help="Sync cached info with Fedora Updates System",
        action="store_true",
    )

    # limit = 5 (default)
    parser.add_argument(
        "-l",
        "--limit",
        help="Maximum limit on number of packages shown for package search",
        default="5",
        nargs=1,
    )
    parser.add_argument(
        "--moreinfo",
        help="Verbose (More Info) in Update Info",
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Name of the package",
        nargs=1,
    )
    parser.add_argument(
        "--noconfig",
        help="Do not check for config file",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--release",
        help="Checks package status for corresponding Fedora release",
        default="f",
        nargs=1,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose output",
        action="store_true",
    )
    parser.add_argument(
        "--version",
        help="gpkgstatus version",
        action="version",
        version=__version__,
    )
    args = parser.parse_args()

    search_pkg(vars(args))
